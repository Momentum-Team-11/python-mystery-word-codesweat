# select random word from words.txt
# import random module **
# open txt file using with syntax **
# put words from txt file into list of strings **
# select one word from list to use for testing **

# show mystery word as underscores to user **
# ask for user guess (upper or lowercase does not matter)
# validate user input if user enters more than one letter
# show user error: "You can only guess letter a a time. Guess again: "

# Show user if guess is part of word **
# replace underscore with letter **
# Show letters that have not been guessed


# limit number of user guesses to 8
# keep track of user guess count
# show user how many guesses are left
# user only loses guess if guess is incorrect
# display mystery word if user runs out of guesses
# show user error if they guess same letter twice. Do not count as a guess in this case.

# Prompt user to play again when the game ends
# Add levels of difficulty based on random word length
# add fun colors if time allows

import random

from pyparsing import WordStart
words = []
underscores = []
guesses = [8]
tries = 8
end_game = False

name = input("What shall I call you? ")
print("Good luck", name, "and have fun!")
print("Guess the Mystery Word")

with open('words.txt') as file:
    # why can't i link this to test-word??
    strings = file.readlines()

    for string in strings:
        words.append(string)
    random_word = words[999].upper()
    random_word = random_word.replace("\n", "")
    print("preview word", random_word)

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_')
    underscores = "".join(underscores)

    print(underscores)
    user_input = input('Guess a letter... ').lower()

    while tries > 0:
        failed = 0

        #for char in random_word:
         #   if char in guesses:
          #      print(char, end=" ")

           # else:
            #    print("_")
             #   print(char, end=" ")

              #  failed += 1

        if failed == 0:
            print("Yay!")
            break

        print()
        guess = input("Guess a letter...")

        guesses += guess

        if guess not in random_word:
            tries -= 1
            print("Oops! Wrong")
            print("You have", + tries, 'more guesses')

            if tries == 0:
                print("You lose.")

    print(underscores)
    user_input = input('Guess again... ')

while user_input != 'Quit' and end_game == False:
        # how can I standize the user input so that no matter what is entered the game stops
# if the user guesses beyond the given amount of tries then set end_game to true
# figure out how to let the user know they've already guessed a letter

# this block is replacing the underscore with the letter guessed if the letter is correct
    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + \
                user_input + underscores[index+1:]
    print(underscores)
    user_input = input('Guess again... ')
# figure out how to end game if user guesses correctly

    if user_input == 'Quit':
        end_game = True

# figure out how to get the game to quit the first time - currently requires 2 quit inputs
# how would using dundermain change my code? investigte if time allows, ask amy
