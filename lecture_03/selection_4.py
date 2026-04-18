
height = float(input("Enter your height in cm: "))

if height >= 400 or height <= 10:
    print("The height is invalid")
else:
    print(f"You are {height/100:.2f} m tall.")