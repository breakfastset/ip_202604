import random
MIN_NUMBER = 1
MAX_NUMBER = 10

def play_game():
    game_over = False
    num_guesses = 0
    guesses = []

    # 1. generate a random number
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    while not game_over:
        print("Previous guesses: ", guesses)

        # 2. ask the user to guess a number
        guess = int(input(f"Guess {MIN_NUMBER} to {MAX_NUMBER}: "))
        num_guesses = num_guesses + 1   # keep track of the guesses
        if not guess in guesses:
            guesses.append(guess)
            guesses.sort()
        else:
            print(f"You already guessed {guess} before! Don't waste my time!")

        # 3. if number is too high
        if guess > answer:
            print("Guess is too high")
        elif guess < answer:
            print("Guess is too low")
        else:
            print("Guess is correct")
            game_over = True

    return num_guesses   # return number of times user has guessed as a feedback


def main():
    another_game = True
    while another_game:
        num_guesses = play_game()
        print(f"You made a total of {num_guesses} guesses for this game.")
        response = input("Do you want to play again? (y/n): ")
        if response.lower() == "n":
            another_game = False

    print("--- Thank you for playing! ---")

if __name__ == '__main__':
    main()