
from account.models import Account
from blockchain.blockchain_explorer import Blockchain


class Build:
    def __init__(self):
        self.chain = "eth"
        self.api = Blockchain(chain=self.chain, network="ganache")

    def create_accounts(self):
        accounts = self.api.w3.eth.accounts

        private_keys = [
            '0xc1784d818f82b8e0f4e2dc5bb98d7cdbdc893785c79d9fe9a4e823eda7bd7cbd',
            '0x59da1b650d2eee346319213f68a2feaf43b7c9c6d7b460b8500f61d865d93211',
            '0x7cfbdde5c3e0a5cc7db6c88059732123e70fd71f51ffd8a5d7b2bb85e493b23b',
            '0xf4b0c9839cd18a5852c662357a4ea7db8380f124ba00b8606da4ad09290bae36',
            '0x378fe10037c76f4640a2c73250fc1033327342a2d42a03c45ecaa41e75659c86',
            '0x6cf50c2c289f0ef942ab06961c42b943a5dae234ccb3d480578442b250e63b1b',
            '0xb28687c0631c004b5c3c6d05e05133713f0a12de8cb9943f0885dcd94d0228df',
            '0x216d2cb7189d3b6927229d54a3198a642ab36894128d59426575634385a9ee1a',
            '0xf4fe9487e142916ae33ecc2c232aba408597955da3b850a62c2aab8f578e544f',
            '0xe3399becabb2204aaa516482698704572185d70c1543406f59299855d33399fb',
        ]

        names = ["Alice", "Bob", "Charlie", "Dan", "Emelia", "Fred", "Greg", "Helen", "Ivan", "Julia", ]

        upload_list = list()
        for index, (account, private_key, name) in enumerate(zip(accounts, private_keys, names)):
            upload_list.append(
                Account(
                    address=account,
                    private_key=private_key,
                    index=index,
                    name=name,
                    chain=self.chain,
                )
            )

        Account.objects.bulk_create(upload_list)





