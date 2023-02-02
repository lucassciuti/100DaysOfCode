import random

from hangman_art import stages, word_list, logo

print(logo)

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Empty list called display
display = ["_" for letter in chosen_word]

end_of_game = False
lifes = len(stages)
stage_step = 0

while not end_of_game:

    # Ask the user to guess a letter
    guess = input('Guess a letter:\n').lower()

    if guess not in chosen_word:
        lifes -= 1
        print(stages[stage_step])
        stage_step += 1
        if lifes == 0:
            end_of_game = True
            print("You lose!")

    else:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = letter

        print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
