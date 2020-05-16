#continuar..

import datetime


class Client:

    def __init__(self, first, last, cpf):
        self.first = first
        self.last = last
        self.cpf = str(cpf)


class Historic:

    def __init__(self):
        self.open_date = datetime.datetime.today()
        self.transactions = []

    def prints(self):
        print(f"Open date: {self.open_date}")
        print("Transactions: ")
        for t in self.transactions:
            print("-", t)


class Account:

    def __init__(self, number, client, balance, limit=1000.0):
        if not isinstance(client, Client):
            raise TypeError(f"client must be of type Client not {type(client)}")
        self._holder = client
        self._number = str(number)
        self._balance = float(balance)
        self._limit = float(limit)
        self._historic = Historic()

    def deposit(self, amount):
        self._balance += amount
        self._historic.transactions.append(f"Deposit of R$ {amount}")

    def withdraw_money(self, amount):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount
            self._historic.transactions.append(f"Cash withdraw of R$ {amount}")

    def bank_statement(self):
        print(f"Account number: {self._number}\n Account balance: {self._balance}")
        self._historic.transactions.append(f"Took extract - Balance of {self._balance}")
        return self._balance

    def transfer_to(self, destiny, amount):
        withdrew = self.withdraw_money(amount)
        if withdrew == False:
            return False
        else:
            destiny.deposit(amount)
            self._historic.transactions.append(f"Transfer of R$ {amount} for account {destiny.deposit}")
            return True

    def update(self, tax):
        self._balance += self._balance * tax


class SavingAccount(Account):

    def __init__(self, number, client, balance, limit=1000.0):
        super().__init__(number, client, balance, limit)

    def update(self, tax):
        self._balance += self._balance * tax * 3


class CheckingAccount(Account):

    def __init__(self, number, client, balance, limit=1000.0):
        super().__init__(number, client, balance, limit)

    def update(self, tax):
        self._balance += self._balance * tax * 2

    def deposit(self, amount):
        self._balance += amount - 0.10
