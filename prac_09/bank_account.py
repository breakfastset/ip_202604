class BankAccount:
    """Simulate a Bank Account."""

    def __init__(self, account_number, balance=0):
        """Initialize the Bank Account with balance set to 0 by default."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit an amount into the Bank Account, return True if successful."""
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """Withdraw an amount from the Bank Account, return True if successful."""
        if amount <= 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def __str__(self):
        """Return a string representation of the Bank Account."""
        return f"Bank Account Number: {self.account_number}\nBalance: ${self.balance:.2f}"


if __name__ == '__main__':
    account_1 = BankAccount(account_number=1005, balance=3000)
    print(account_1)
    account_2 = BankAccount(account_number=1006)
    print(account_2)
    print()
    print("1. Attempting to deposit $0 into acct 1005")
    if account_1.deposit(0):
        print("Successfully deposited $0 into acct 1005")
    else:
        print("Failed to deposit $0 into acct 1005")
    print(account_1)

    print()
    print("2. Attempting to deposit $500 into acct 1005")
    if account_1.deposit(500):
        print("Successfully deposited $500 into acct 1005")
    else:
        print("Failed to deposit $500 into acct 1005")
    print(account_1)

    print()
    print("3. Attempting to withdraw $10000 from acct 1005")
    if account_1.withdraw(10000):
        print("Successfully withdrawn $10000 from acct 1005")
    else:
        print("Failed to withdraw $10000 from acct 1005")
    print(account_1)
