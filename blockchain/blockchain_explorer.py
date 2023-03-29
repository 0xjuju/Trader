
from abc import ABC
from decimal import Decimal
from typing import Union

from blockchain.errors import *
from decouple import config
from eth_typing.evm import ChecksumAddress
from web3 import (Web3)
from web3.contract import Contract


class Transaction:
    def __init__(self, transaction_data: dict):
        """
        :param transaction_data: key-value pairs of options for building a transactions
        """
        self.data = dict()
        REQUIRED_FIELDS = ["nonce", "gas", "gasPrice", "value"]

        for key, value in transaction_data.items():
            key = "from" if key == "from_address" else key  # can't use the 'from' keyword for Python but need it for tx
            self.data[key] = value

        keys = self.data.keys()

        for field in REQUIRED_FIELDS:
            if field not in keys:
                raise ValueError(f"Transaction must include the following key {field}")

        if "to" not in keys and "from" not in keys:
            raise ValueError("Transaction must include at least a 'to' value or a 'from' value")

        if "to" in keys:
            error_if_not_checksum_address(self.data["to"])
        elif "from" in keys:
            error_if_not_checksum_address(self.data["from"])


class BlockchainOperations(ABC):

    @staticmethod
    def build_transaction(sender_address: ChecksumAddress, gas_price: float, value: float, gas=3_000_000,
                          from_address: ChecksumAddress = None, to_address: ChecksumAddress = None) -> Transaction:

        transaction = {
            "nonce": Web3.eth.get_transaction_count(sender_address),
            "value": Web3.to_wei(value, 'ether'),
            "gas": gas,
            "gasPrice": Web3.to_wei(gas_price, 'gwei'),
        }

        if from_address:
            transaction["from"] = from_address
        if to_address:
            transaction["to"] = to_address

        tx = Transaction(transaction_data=transaction)
        return tx

    @staticmethod
    def convert_balance_to_eth(*, balance, decimals: int) -> Decimal:
        """
        :param balance: value to convert
        :param decimals: number of decimals for currency
        :return:
        """
        balance = Decimal(balance)
        return Decimal(balance / (10 ** decimals))

    @staticmethod
    def sign_transaction(transaction: Transaction, signer_address: ChecksumAddress) -> str:
        signed_transaction = Web3.eth.sign_transaction(transaction.data, signer_address)
        tx_hash = Web3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        return tx_hash.decode()


class Blockchain(BlockchainOperations):

    def __init__(self, chain, network="mainnet", version=3):
        self.chain = chain
        self.network = network
        self.base_url = f"infura.io/v{version}/{config('INFURA_KEY')}"
        self.w3 = self.set_connection()

    def get_balance(self, address: ChecksumAddress, token_contract=None, currency_format="wei"):
        """
        :param address: wallet address
        :param token_contract: contract of token to check balance. Default to ETH balance
        :param currency_format: Ether denomination
        :return:
        """

        if token_contract:
            balance = token_contract.functions.balanceOf(address).call()
        else:
            balance = self.w3.eth.get_balance(address)

        if currency_format != 'wei':
            balance = self.w3.from_wei(balance, currency_format)

        return balance

    def get_provider(self):

        valid_networks = ["mainnet", "goerli", "sepolia", "fuji", "mumbai", "testnet", "ganache"]

        if self.network not in valid_networks:
            raise ValueError(f"{self.network} not a valid network. Options are {valid_networks}")

        if self.network == "ganache":
            return 'http://127.0.0.1:7545'

        else:
            protocol = "https://"

            providers = {
                "eth": f"{protocol}{self.network}.{self.base_url}",
                "polygon": f"{protocol}polygon-{self.network}.{self.base_url}",
                "arbitrum": f"{protocol}arbitrum-{self.network}.{self.base_url}",
                "optimism": f"{protocol}optimism-{self.network}.{self.base_url}",
                "palm": f"{protocol}palm-{self.network}.{self.base_url}",
                "avalanche": f"{protocol}avalanche-{self.network}.{self.base_url}",
            }

            provider = providers.get(self.chain)

        if provider:
            return provider
        else:
            raise ValueError(f"Invalid provider ({provider}). Options are: {providers.keys()}")

    def set_connection(self):

        if self.chain != "bsc":
            rpc_url = self.get_provider()
            connection = Web3(Web3.HTTPProvider(rpc_url))

        else:
            # RPC_URL = "wss://bsc-ws-node.nariox.org:443"
            rpc_url = "https://bsc-dataseed.binance.org/"

            connection = Web3(Web3.HTTPProvider(
                rpc_url,
            ))

        return connection

