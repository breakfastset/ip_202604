import random

def shift_coordinates(x, y, amount):
    x = x + amount
    y = y + amount
    return x, y

def main():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    amount = random.randint(1, 20)
    print("Original coordinates:")
    print(f"({x}, {y})")
    print("Shifted coordinates:")
    new_x, new_y = shift_coordinates(x, y, amount)
    print(f"({new_x}, {new_y})")

main()