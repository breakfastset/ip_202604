# Write a program to ask for a purchase amount and the number of instalments.
# Add 5 percent to the amount as interest.
# Get the nett amount and divide by the number of instalments requested.
# Finally, display the purchase amount cum interest, and instalment amount.

INTEREST_RATE = 0.05
purchase_amount = float(input("Purchase amount: "))
num_instalments = int(input("Number of instalments (<= 12): "))
nett_amount = purchase_amount * (1 + INTEREST_RATE)

instalment = nett_amount / num_instalments

print(f"   Purchase amount: ${purchase_amount:,.2f}")
print(f"       Nett amount: ${nett_amount:,.2f} ")
print(f"Monthly instalment: ${instalment:,.2f}")