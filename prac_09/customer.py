from prac_09.bank_account import BankAccount


class Customer:

    def __init__(self, customer_id, name):
        """Initialise Customer attributes."""
        self.customer_id = customer_id
        self.name = name
        self.bank_accounts = []

    def add_bank_account(self, bank_account_number, balance=0):
        """Add a BankAccount object to its list."""
        if balance < 0:
            balance = 0
        new_bank_account = BankAccount(bank_account_number, balance)
        self.bank_accounts.append(new_bank_account)

    def deposit(self, bank_account_number, amount):
        """Deposit amount to own BankAccount with bank account number."""
        has_deposited = False
        if amount > 0:
            index = 0
            while index < len(self.bank_accounts) and has_deposited == False:
                current_bank_account = self.bank_accounts[index]
                if current_bank_account.account_number == bank_account_number:
                    has_deposited = True
                    current_bank_account.deposit(amount)
                index += 1

        return has_deposited

    def withdraw(self, bank_account_number, amount):
        """Withdraw amount from own BankAccount with bank account number."""
        has_withdrawn = False
        if amount > 0:
            index = 0
            while index < len(self.bank_accounts) and has_withdrawn == False:
                current_bank_account = self.bank_accounts[index]
                if current_bank_account.account_number == bank_account_number:
                    if amount <= current_bank_account.balance:
                        has_withdrawn = True
                        current_bank_account.withdraw(amount)
                index += 1

        return has_withdrawn

    def __str__(self):
        """Return a string representation of the Customer object."""
        details = (f"Customer Id: {self.customer_id}"
                   f"\nCustomer Name: {self.name}")
        details += "\n--Bank Accounts--\n"
        for bank_account in self.bank_accounts:
            details += str(bank_account) + "\n"
        return details

if __name__ == '__main__':
    my_customer = Customer(5888, "Ronald Duck")
    my_customer.add_bank_account("1005", 100)
    my_customer.add_bank_account("1006")
    my_customer.add_bank_account("1007", 5555)
    print(my_customer)
    print()
    print("Trying to deposit $1000 into bank account 1006")
    my_customer.deposit("1006", 1000)
    print(my_customer)
    print()
    print("Trying to deposit $2000 into bank account 1008")
    my_customer.deposit("1008", 2000)
    print(my_customer)
    print("Trying to withdraw $2000 from bank account 1007")
    my_customer.withdraw("1007", 2000)
    print(my_customer)