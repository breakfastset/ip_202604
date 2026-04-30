
def add_three(a, b, c):
    total = a + b + c
    print(total)

def change_this(x):
    print(f"Value of argument: {x}")
    print("Changing to +100")
    x = x + 100

def announce_winners(champion, first_runner_up, second_runner_up):
    print(f"The 2nd runner up is: {second_runner_up}")
    print(f"The champion is: {champion}")
    print(f"1st runner up is: {first_runner_up}")

def main():
    add_three(5, 6, 7)    # 18
    number = 99
    change_this(number)  # pass by value
    print("Number after changing: ", number)

    runnerup_1 = "Lucky"
    runnerup_2 = "Brave"
    champ = "Champ"
    announce_winners(first_runner_up=runnerup_1,
                     second_runner_up=runnerup_2,
                     champion=champ)

main()  # Call main