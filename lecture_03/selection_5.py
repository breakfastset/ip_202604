age = 21
is_working = False
amount = 0

if age >= 65 and not is_working:
    amount = 1000
elif age >= 65 and is_working:
    amount = 600
elif age >= 21 and not is_working:
    amount = 500
elif age >= 21 and is_working:
    amount = 200

print(f"You will receive ${amount}")
print("----------------------------")
if age >= 65:
    if is_working:
        amount = 600
    else:
        amount = 1000
elif age >= 21:
    if is_working:
        amount = 200
    else:
        amount = 500