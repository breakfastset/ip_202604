print("-- Cashier --")
amount = float(input("How much spent? "))

if amount > 200:
    print("Oh you spent more than $200!")
    print("Applying discount....")
    amount = amount * 0.95   # statement is part of if

print(f"You need to pay ${amount:.2f}")  # not part of if