import random


def generate_answer(word_list):
    """Generate a word from a list."""
    word_index = random.randint(0, len(word_list) - 1)
    answer = word_list[word_index]
    return answer   # a string   # docstring

def save_roll_of_honour(number_of_wins):
    """Ask the user for a name, to write to the file."""
    pass

def display_word(answer, list_of_guesses):
    """Display the current word in dashes or characters guessed correctly."""
    for char in answer:
        if char in list_of_guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def make_a_guess(list_of_guesses):
    """Make a guess and if it is 1 char, append to list if not found."""
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        print("!! Please enter a single letter")
    elif guess not in list_of_guesses:
        list_of_guesses.append(guess)
    else:
        print("!! Guess is already in the list.")

def determine_game_won(word, list_of_guesses):
    """Determine if the game is won."""
    has_won = True
    count = 0
    while count < len(word) and has_won == True:
        if not word[count] in list_of_guesses:
            has_won = False
        count = count + 1
    return has_won

def play_game(word_list):
    """Play a Hangman game."""
    answer = generate_answer(word_list)

    game_over = False
    list_of_guesses = []
    while not game_over:
        # 1. display the word in dashes
        display_word(answer, list_of_guesses)

        # 3. ask the user for a guess
        make_a_guess(list_of_guesses)

        game_over = determine_game_won(answer, list_of_guesses)

    print(f"The word is {answer}")
    print("You have won!")


def read_words():
    """Read the words from file into a list."""
    word_list = []
    in_file = open("hangman_words.txt", "r")
    for line in in_file:
        word_list.append(line.strip())
    in_file.close()
    return word_list


def main():
    """Start program."""
    word_list = read_words()    # generate list from a file.
    play_game(word_list)

if __name__ == '__main__':
    main()


# Other features:
# 1. give 5 lives per game
# 2. allow user to play again
# 3. keep track of the number of times won and lost
# 4. save the high score (for top 3 winners)
# 5. draw the hangman











