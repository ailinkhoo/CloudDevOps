# A simple number guessing game
# Could you make something cooler?
import random # module, library

# Make n a random number between 1 and 99
n = random.randint(1, 99)

# Ask user to guess the number
try:
    while n != "guess": # while loop that continues as long as the input is different from the random number
        guess = int(input("Enter an integer from 1 to 99: "))
        if guess > 99 or guess < 1: # check if the user entered a number within the given range
            print ("out of range")
        elif guess < n:
            print ("guess is low")
        elif guess > n: 
            print ("guess is high")
        else:
            print ("you guessed it!")
            break #break out of the while loop
except:
    print('Error, please enter numeric input')
     
"""
Try and Except statement is used to handle these errors within our code in Python. 
The try block is used to check some code for errors i.e the code inside the try 
block will execute when there is no error in the program. Whereas the code inside 
the except block will execute whenever the program encounters some error in the preceding try block.
"""
