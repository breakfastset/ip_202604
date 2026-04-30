seatings = [
    ["Siti", "Lawrence", "Kimchi"],   # row 0
    ["Hassan", "Ah Teo", "Ming"],     # row 1
    ["Vicky", "Peter", "Ara"],        # row 2
    ["Mew", "Mewtwo", "Mewthree"]     # row 3
]   # 0         1           2  <- columns

print(seatings[0][0])    # Siti  row 0, column 0
print(seatings[2][1])    # Peter row 2, column 1
print("---" * 10)

for row in range(len(seatings)):   # 4 rows
    print("=" * 36)      # start of row
    for col in range(len(seatings[row])):
        print(f"{seatings[row][col]:12}", end="")
    print()  # end of the row
print("=" * 36)