"""
This program will try to predict a secret number from 1 to 20 and asl the user to guess it. 
After each guess, the computer will tell the user whether the number is too high or too low. 
The user wins if they can guess the number within six tries. 
"""

import random

guessesTaken = 0

print("Hello, there! What is your name?")

myname = input("Enter your name: ")
print("Nice to meet you" + myname)

number = random.randint(1, 20)
print('Well' + myname + 'I am gussing a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('Good job, ' + myname +
          '! You guessed the right number in ' + guessesTaken + 'guesses!')

if guess != number:
    numnber = str(number)
    print('Nope. The nymber I was thinking of was' + number + '.')

"""
User notes: The program runs but the loop at line 38 shows error and does not break.
            As a result the desired output can not be reached.
"""
