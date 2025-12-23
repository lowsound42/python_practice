import random

hero_list = ["batman", "iron man", "superman", "black panther"]
chosen_word = random.choice(hero_list)
guessed_letters = []
game_over = False


def display_blanks():
    for i in chosen_word:
        if i == " ":
            print(" ", end="")
        else:
            print("_", end="")
    print("")


def display_guesses():
    num_remaining = 0
    for i in chosen_word:
        if i == " ":
            print(" ", end="")
        elif i in guessed_letters:
            print(i, end="")
        else:
            num_remaining += 1
            print("_", end="")
    print("")
    if num_remaining == 0:
        return True
    else:
        return False


def add_letter_to_guesses(letter):
    if len(letter) == 1 and letter.isalpha():
        if letter not in guessed_letters:
            guessed_letters.append(letter)
        return True
    else:
        return False


display_blanks()

while not game_over:
    guess = input("guess a letter: ").lower()
    check = add_letter_to_guesses(guess)
    while not check:
        guess = input("That was an invalid input, try again: ")
        check = add_letter_to_guesses(guess)
    game_over = display_guesses()
