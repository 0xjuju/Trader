from eth_typing.evm import Address, ChecksumAddress
from web3 import Web3


def error_if_not_checksum_address(address):
    if not Web3.is_checksum_address(address):
        raise ValueError(f"{address} must be a Checksum address")


