
try:
    height = float(input("Enter your height: "))
    print(f"You are {height:.1f} m tall")
except ValueError:
    print("Please enter a number only")

print("Thank you")