# an acceptable age is between 21 to 120

valid_age = False
while not valid_age:   # valid_age == False
    age = int(input("Please enter your age: "))
    if 21 <= age <= 120:
        valid_age = True
    else:
        print("Age must be between 21 and 120!")
        print("Try again!")

print(f"Hi you will be {age + 1} next year!")