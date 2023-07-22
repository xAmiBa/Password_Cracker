import string
import time
import random


# User inputs a password to crack
password = input("Write down your password: ")
print()
print("Thank you! Your password's security is being checked...")
print()

guess = ""  # Variable will contain cracked password
length = len(password)  # The length of the input
characters = string.ascii_letters + string.digits + string.punctuation  # Strings generated by string library
character_list = list(characters)  # Sll possible password characters
start_time = time.time()  # Loop start time
timeout = time.time() + 60  # Loop termination time
attempts = 0  # Number of randomly generated passwords by brute force loop

"""
This while loop is repeating a block of code which guesses the password.
The loop continues while "guess" is not equal to user input "password" 
and loop termination time (60sec) did not pass.
The while loop:
- adds up attempt number with each loop
- generates random guesses in length of input
- adds result to "guess" variable
- compares "guess" variable with "password" variable
"""

while (guess != password) and timeout > time.time():
    attempts = attempts + 1
    # random.choices method generates random results from specific variable
    # par1 is variable, par2 = k is length of returned list
    guess = random.choices(character_list, k=length)
    guess = "".join(guess)

    # Notify user if password is cracked wuthin 60 sec. Prints time it took and attempts number.
    if guess == password:
        print("Your password has been cracked! You need more secure password than \"" + guess + "\".")
        print()
        print("It took %s seconds to hack it!" % (time.time() - start_time))
        print()
        print(f"I guessed it in {attempts:,} attempts.")
        print()
        print("For the sake of safety, let's improve your password!")
        print()

# Notify user when loop terminated after 60sec and program was unable to crack password on time.
if timeout <= time.time():
    print("I couldn't hack your password in less than 60sec!")
    print()
    print("Unfortunately hackers might have faster computer, I think we should check how secure it is!")
    print()

# Print dividers and empty lines for readability
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *")
print()

