response = "y"   # 1. init

while response.lower() == "y":   # 2. condition
    print("==== Commission Calculator ====")   # 3. statements
    #
    sales = float(input("Enter the sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    commission = sales * comm_rate
    print(f"You earn ${commission:.2f}")
    #
    response = input("Continue? (y/n): ")  # 4. update

print("Thank you!")
# sentinel value, 'y'