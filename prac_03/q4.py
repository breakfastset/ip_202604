# Write a program that asks the user for a month as a number between 1 and 12.
# The program should display a message indicating whether the month is in the first quarter,
# the second quarter, the third quarter, or the fourth quarter of the year. Following are the guidelines:
# • If the user enters either 1, 2, or 3, the month is in the first quarter.
# • If the user enters a number between 4 and 6, the month is in the second quarter.
# • If the number is either 7, 8, or 9, the month is in the third quarter.
# • If the month is between 10 and 12, the month is in the fourth quarter.
# • If the number is not between 1 and 12, the program should display an error.

month = int(input("Month? "))

if 1 <= month <= 3:
    quarter = 1
elif 4 <= month <= 6:
    quarter = 2
elif 7 <= month <= 9:
    quarter = 3
elif 10 <= month <= 12:
    quarter = 4
else:
    quarter = 0    # let quarter be 0

if quarter == 0:   # if quarter is 0
    print("Invalid month entered!")
else:
    print(f"Month {month} is in the {quarter} quarter!")