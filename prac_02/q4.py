SALES_TAX_RATE = 0.07

item_1_price = float(input("Enter item 1 price: "))
item_2_price = float(input("Enter item 2 price: "))
item_3_price = float(input("Enter item 3 price: "))
item_4_price = float(input("Enter item 4 price: "))
item_5_price = float(input("Enter item 5 price: "))

total_amount = (item_1_price + item_2_price + item_3_price
                + item_4_price + item_5_price)
sales_tax = SALES_TAX_RATE * total_amount
nett_amount = total_amount + sales_tax

print(f"Total amount before tax: ${total_amount:.2f}")
print(f"              Sales tax: ${sales_tax:.2f}")
print(f"            Nett amount: ${nett_amount:.2f}")