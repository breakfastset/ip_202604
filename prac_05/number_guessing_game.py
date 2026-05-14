import random

def play_game():
    game_over = False
    # 1. generate a random number
    answer = random.randint(1, 100)
    while not game_over:
        # 2. ask the user to guess a number
        guess = int(input("Guess 1 to 100: "))
        # 3. if number is too high
        if guess > answer:
            print("Guess is too high")
        elif guess < answer:
            print("Guess is too low")
        else:
            print("Guess is correct")
            game_over = True

def main():
    another_game = True
    while another_game:
        play_game()
        response = input("Do you want to play again? (y/n): ")
        if response.lower() == "n":
            another_game = False

    print("--- Thank you for playing! ---")

if __name__ == '__main__':
    main()