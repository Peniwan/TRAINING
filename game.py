""""create a simple number guessing game where the computer randomly
selects a number between 1 and 100 and the user has to guess it.
The game should provide feedback to the user if their guess is too high,
too low, or correct. Once the user guesses correctly, the game should end and display the number of attempts it looks."""

"""numbers=[10, 45, 55, 70, 88, 97, 120 ]
if numbers <='100':
   numbers= print("guess the numbers")
   x=int (input("whats the guess number"))

if x<= '100':
   print ("x is correct")
elif x> '100':
   print("x is high")
else:
    print("x is low")"""

import random

print ("welcome to number guessing game")
print("I have selected random numbers from 1 to 100, can you guess it")

random_number=random.randint(1, 100)
attempt=0
while True:
    Guess_number=int(input("what is your guess number "))
    attempt=attempt+1

    if Guess_number<random_number:
        print("number is too low" )

    elif Guess_number>random_number:
        print("number is too high" )

    else:
        print(f"congratulations you guess the correct answer. The correct guess number is {random_number}" ) 
        print(f"the number of attempts is {attempt}")
        break

      






     

