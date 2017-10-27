"""Bull & cow game. Guessing a four unique digit number.
"""

import random
import sys

#Create a random four unique digit number (list of str).
number_to_guess = [str(x) for x in random.sample(set(range(10)), 4)]
game = True #Boolean for the while loop


def check_guess(guess):
    """Check player's guess and give feedback.

    Args:
        guess: Player's guess, a string of ints.

    Returns:
        bull: The correct digit at the correct position.
        cow: The correct digit at a wrong position.
    """
    global game
    bull = 0
    cow = 0
    for digit in guess:
        if digit == number_to_guess[guess.index(digit)]:
            bull += 1
        elif digit in number_to_guess:
            cow += 1
    if bull == 4: #Winning scenario, stop the game
        game = False
    return bull, cow


def main():
    #print(number_to_guess) for debuggung
    print("Guess a four unique digit number!\n"
            "'Bull' is the right digit at the right position.\n"
            "'Cow' is the right digit at a wrong position.\n"
            "Example: if the number is 1234 and your guess is 5304, then..\n"
            "4 is a bull and 3 is a cow.")
    print('-' * 25)
    while game:
        guess = input()
        #I want to have the feedback of player's guesses right after the guess
        # and on the same line, so it doesn't cut into the numbers' column
        #It is also a natural positioning when you play the game on paper.
        bull, cow = check_guess(guess) #unpacking for print
        sys.stdout.write("\033[F") #move the cursor up one line
        print(("{0} - {1} bull(s) {2} cow(s)").format(guess, bull, cow))
    print('You won!') #You can't lose, you can give up :)


if __name__ == '__main__':
    main()
