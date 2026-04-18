POOR_THRESHOLD = 1643.50
per_head_income = float(input("Enter your per-head income: "))
housing_type = input("Public or Private: ")

if per_head_income < POOR_THRESHOLD and housing_type.lower() == "public":
    print("You are eligible for financial aid of $500 per head per month.")
else:
    print("Unfortunately you do not meet the requirements for aid.")

print()
print()
response_1 = input("Are you a student in PSB? (y/n) ")
response_2 = input("Are you a staff in Marina Center? (y/n) ")

if response_1.lower() == "y" or response_2.lower() == "y":
    print("You are entitled to 15% discount.")
else:
    print("Sorry the discount is for students or staff only.")

print()
temperature = 70
if not (temperature > 100):    # if temperature <= 100:
    print("Temperature is 100 and below")

is_happy = False

if not is_happy:     # if is_happy == False:
    print("Let's go for a run")
else:
    print("Let's go watch a movie")





