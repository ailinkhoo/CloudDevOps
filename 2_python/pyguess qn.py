# A simple number guessing game
# Could you make something cooler?
import random

# Make n a random number between 1 and 99
n = random.randint(1, 99)

# Ask user to guess the number
guess = int(input("Enter an integer from 1 to 99: "))

while n != "guess":
    print
    if guess < n: 
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n: 
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break
    print

