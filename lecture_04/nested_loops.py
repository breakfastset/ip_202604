# 3x times table

for row in range(1, 13):   # from 1 to 12
    # --- start of row ---- #
    for col in range(1, 11):   # from 1 to 10
        print(f"{row * col:3}", end=" ")  # print on same line
    print()   # terminate the row with a new line
    # ---- end of row ----- #