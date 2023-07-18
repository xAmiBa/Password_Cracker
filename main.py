import random
import string
import time

# User inputs password -> str
password = input("Write down your password: ")

#time measurment starts
start_time = time.time()

print("Thank you! Your password's security is being checked... Look below for presonalised report.")
print()

# *** loading dots animation ***
# Bruce force attack with use of Bruce force algorythm

#password guessing variables
guess = ""
length = len(password)
characters = string.ascii_letters + string.digits + string.punctuation
character_list = list(characters)

#timimg variables
timeout = time.time() + 60

while (guess != password):
    # random.coices method generates random results from specific list, k parameter is lenght of returned list
    guess = random.choices(character_list, k=length)
    guess = "".join(guess)

# Cracked password output
else:
    print("Your password has been cracked! You need more secure password than \"" + guess + "\".")

# If cracked: Time

print("It took %s seconds to hack it!" % (time.time() - start_time))

# ***Time limit to cracking? Make python stop after 60 sec
#print("It took too long to crack it!")

# If cracked: Attempts number

# User input: Do you want to generate safer password?
# If cracked: Safety aid algorythm


#

#

#

#