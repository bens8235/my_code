import random
from Hangman_images import logo, stages
from Hangman_words import word_list

print(logo)

# Choosing a random word out of the word_list or choose own word:

chosen_word = random.choice(word_list)
# chosen_word = "hello"

# Setting variables that I will need later.
# Empty list to add blanks to, depending on how many letters in the word.
# Starting lives for the game.
# Setting the game to run to be True, so it will keep running until this becomes False.
# Setting the guess to be false initially to have the option to change it to True for a correct guess.
# Empty list to add incorrect letters to keep track of guesses.

display = []
lives = 7
game_run = True
correct_guess = False
incorrect_letters = []

# Looping through all the letters in chosen_word then adding a blank tile for each letter in word to my "display" list:

for letter in chosen_word:
    if letter == " ":
        display.append("space")
        continue
    display.append("_")

# While game_run is set to True the below code will run until it changes to False
# Starting counter at -1 so that when we loop through the chosen word the counter will then be at 0.
# Prints number of blank tiles.
# User to input their chosen letter then check if that letter in chosen word.
# We will tell user if they have already guessed it.
# Looking at all the letters in the chosen word and for each letter make the count equal the index.
# If the user guess equals a letter in the word the list display will replace a blank with the letter.
# It will then set correct_guess to True.

while game_run:
    count = -1
    print(display)
    guess = input("Guess a letter? ").lower()
    if guess in display:
        print("You have already guessed " + guess)
    for i in chosen_word:
        count = count + 1
        if guess == i:
            display[count] = i
            correct_guess = True

    # If guess does not match any of the letters correct_guess will still be false so tell the user they lose a life.
    # Take away a life. Show them the next stage of the diagram and show them a list of incorrect letters so far.

    if correct_guess == False:
        print("You guessed " + guess + " that's not in the word. You lose a life.")
        lives = lives - 1
        print(stages[lives])
        incorrect_letters.append(guess)
        print("The incorrect letters you have chosen so far are: ", incorrect_letters)

    # Need to set correct_guess back to False for the next loop.
    # If there are no blanks left in display list the game_run will be set to false and the loop will stop. User wins.
    # If there are no more lives the game will also stop and tell the user they lose.

    correct_guess = False
    if "_" not in display:
        game_run = False
        print(display)
        print("You win")
    if lives == 0:
        game_run = False
        print("You Lose")
