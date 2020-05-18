import unittest
from main import Account, CheckingAccount, SavingAccount, Client, InvestmentAccount


class TestMain(unittest.TestCase):
    def setUp(self):
        self.client_1 = Client("Isis", "Padilha", "555.444.777-99")
        self.client_2 = Client("Pedro", "Santos", "444.222.333-11")
        self.client_3 = Client("Mariana", "Nunes", "111.111.111-11")

        self.saving_1 = SavingAccount("123-9", self.client_1, "4000.0")
        self.checking_1 = CheckingAccount("135-6", self.client_2, "6000.0")
        self.investment_1 = InvestmentAccount("1479-6", self.client_3, "7000.0")

    def tearDown(self):
        pass


    def test_update(self):

        self.saving_1.update(0.01)
        self.checking_1.update(0.01)
        self.investment_1.update(0.01)

        self.assertEqual(self.saving_1.bank_statement(), 4120.0)
        self.assertEqual(self.checking_1.bank_statement(), 6120.0)
        self.assertEqual(self.investment_1.bank_statement(), 7350.0)



if __name__ == "__main__":
    unittest.main()