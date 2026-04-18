balance = 5555
RETURN_ON_INVESTMENT = 0.10
num_years = 37

new_balance = balance * ((1 + RETURN_ON_INVESTMENT) ** num_years)

print(f"Original investment : ${balance:12,.2f}")
print(f"My projected balance: ${new_balance:12,.2f}")
print()
print()

title = "My Investment"
label_1 = "Original Investment"
label_2 = "Projected Balance"
print("=" * 56)
print(f"| {title:^52} |")   # caret, circum accent
print("=" * 56)
print(f"| {label_1:>24} | ${balance:<24,.2f} |")
print("-" * 56)
print(f"| {label_2:>24} | ${new_balance:<24,.2f} |")
print("=" * 56)

# strings always align to left by default
# numbers always alignt to right by default