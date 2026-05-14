def determine_game_won(word, list_of_guesses):
    has_won = True
    count = 0
    while count < len(word) and has_won == True:
        if not word[count] in list_of_guesses:
            has_won = False
        count = count + 1
    return has_won

def determine_game_won2(answer, list_of_guesses):
    characters = set(answer)
    characters = sorted(list(characters))
    characters = "".join(characters)
    list_of_guesses.sort()
    guess = "".join(list_of_guesses)
    return characters == guess

def main():
    answer = "apple"
    list_of_guesses = ['a', 'e', 'p', 'l']
    has_won = determine_game_won2(answer, list_of_guesses)
    print(has_won)

if __name__ == '__main__':
    main()