# *                     1
# * *                   2
# * * *                 3
# * * * *
# * * * * *

for row in range(1, 9):            # 8 rows
    # start of the row
    for col in range(1, row+1):        # 8 columns
        print("*", end=" ")
    print()
    # end of the row

