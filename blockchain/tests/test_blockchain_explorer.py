
from account.models import Account
from blockchain.blockchain_explorer import Blockchain, BlockchainOperations, Transaction
from blockchain.tests.build_test_data import Build
from django.test import TestCase


class TestBlockchain(TestCase):

    def setUp(self) -> None:
        b = Build()
        b.create_accounts()

        self.w3 = Blockchain("eth", network="ganache")

    def test_connections(self):
        pass
        # chains = ["eth", "bsc", "polygon", "arbitrum", "optimism", "palm", "avalanche", ]
        # for chain in chains:
        #     blockchain = Blockchain(chain=chain)
        #     self.assertTrue(blockchain.w3.is_connected())

    def test_get_balance(self):
        account = Account.objects.get(index=1)
        balance = self.w3.get_balance(account.address)
        # self.assertEqual(balance, 100 * 10**18)

    def test_transaction_class(self):

        tx = Transaction(
            {
                "nonce": 5,
                "gas": 1,
                "gasPrice": 1,
                "value": 100,
                "from": '0x83C3996d48D97CA14B4e5Dab604F67bf3cDd3E54'
            }
        )

        self.assertEqual(
            tx.data,

            {
                "nonce": 5,
                "gas": 1,
                "gasPrice": 1,
                "value": 100,
                "from": '0x83C3996d48D97CA14B4e5Dab604F67bf3cDd3E54'
            }
        )










