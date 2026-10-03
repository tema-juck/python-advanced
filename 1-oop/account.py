"""Bank Account"""


class BankAccount:
    """Account Class"""
    accounts = []

    def __init__(self, owner: str, account_number: int | str, current_balance: int = 0):
        self.owner = owner
        self.account_number = account_number
        self.current_balance = current_balance
        BankAccount.accounts.append(self)

    def deposit(self, amount: int):
        """Deposit balance"""
        self.current_balance += amount

    def withdraw(self, amount: int):
        """Withdraw balance"""
        if self.current_balance <= 0:
            print(f"У вас на балансе: {self.current_balance}!")

        if (self.current_balance - amount) < 0:
            print(
                f"У вас недостаточно средств на балансе: {self.current_balance}!")

        self.current_balance -= amount

    def transfer_to(self, other_account: BankAccount, amount: int):
        """Transfer Method"""
        if self.current_balance <= 0:
            print(
                f"У вас недостаточно средств на балансе: {self.current_balance}!")
        elif (self.current_balance - amount) < 0:
            print(
                f"У вас недостаточно средств для перевода: {self.current_balance}!")
        else:
            self.current_balance -= amount
            other_account.current_balance += amount

    def info(self):
        """Info about Account"""
        return f"""Текущее информация о счете:
    Владелец счета: {self.owner}
    Баланс: {self.current_balance}
    Номер счета: {self.account_number}
    """

    @classmethod
    def get_accounts_created(cls):
        """get accounts created"""
        return len(cls.accounts)


account1 = BankAccount("Kate", 1122334455, 0)
account2 = BankAccount("Denis", 1122334466, 1000)

account1.transfer_to(account2, 1000)

print(account2.info())
print(account1.info())

print(BankAccount.get_accounts_created())
