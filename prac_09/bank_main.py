from customer import *

MENU="""
--------------------------------
|   PSBank Pte Ltd Main Menu   | 
--------------------------------
1. New customer sign up.
2. Search customer
3. Quit
>> """

SUB_MENU="""
---------------------------------
| 2. Search Customer (Sub menu) |
---------------------------------
1. Add bank account
2. Deposit
3. Show bank accounts
4. Back to main menu
>> """

def search_customer(customers, customer_id):
    """Return Customer object if customer found, None otherwise."""
    index = 0
    found_customer = None

    while index < len(customers) and found_customer is None:
        if customers[index].customer_id == customer_id:
            found_customer = customers[index]
        index += 1
    return found_customer

def search_account(accounts, account_number):
    """Return True if Bank account found, False otherwise."""
    index = 0
    found = False
    while index < len(accounts) and not found:
        if accounts[index] == account_number:
            found = True
        index += 1
    return found

def main():
    """Start of program."""

    customers = []
    bank_account_ids = []
    choice = input(MENU)
    while choice != "3":
        if choice == "1":
            customer_id = int(input("Enter customer id: "))
            if not search_customer(customers, customer_id) is None:
                print("Customer id already exists!")
            else:
                customer_name = input("Enter customer name: ")
                new_customer = Customer(customer_id, customer_name)
                customers.append(new_customer)
                print("New customer added!")
        elif choice == "2":
            customer_id = int(input("Enter customer id: "))
            found_customer = search_customer(customers, customer_id)
            if not found_customer is None:
                sub_choice = input(SUB_MENU)
                if sub_choice == "1":
                    print(f"   --- Adding a bank account to customer id {customer_id}  ---")
                    account_number = int(input("Enter account number: "))
                    if not account_number in bank_account_ids:
                        found_customer.add_bank_account(account_number)
                        print("Account number added!")
                elif sub_choice == "2":
                    pass
                elif sub_choice == "3":
                    print(found_customer)
                else:
                    print("Invalid choice!")
            else:
                print("Customer id does not exist!")
            print()
        choice = input(MENU)
    print("~- Thank you for patronising PSBank -~")


if __name__ == '__main__':
    main()