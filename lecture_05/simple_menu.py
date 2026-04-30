import random

MENU="""1. Get a lucky number
2. Find the ascii code of a char
3. Print ascii table.
4. Quit
>> """

def option_1():
    lucky_number = random.randint(1, 10)
    print("Your lucky number is: ", lucky_number)

def main():
    choice = input(MENU)
    while choice != '4':
        if choice == '1':
            option_1()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print("Invalid choice")
        choice = input(MENU)
    print("Thank you for using our program.")

main()