import random
import string
import time

# User inputs password -> str
password = input("Write down your password: ")




print("Thank you! Your password's security is being checked...")
print()

# Bruce force attack with use of Bruce force algorythm

#password guessing variables
guess = ""
length = len(password)
characters = string.ascii_letters + string.digits + string.punctuation
character_list = list(characters)

#timimg variables
#time measurment starts
start_time = time.time()
timeout = time.time() + 60
attempts = 0

#if timeout > time.time():
while (guess != password) and timeout > time.time():
    attempts = attempts + 1
    # random.choices method generates random results from specific list, k parameter is lenght of returned list
    guess = random.choices(character_list, k=length)
    guess = "".join(guess)


    # Cracked password output
    if guess == password:
        print("Your password has been cracked! You need more secure password than \"" + guess + "\".")
        print()
        # If cracked: Time
        print("It took %s seconds to hack it!" % (time.time() - start_time))
        print()

        # If cracked: Attempts number
        print(f"I guessed it in {attempts} attempts.")
        print()
        print("For the sake of safety, let's improve your password!")
        print()

#Make python stop after 60 sec
if timeout <= time.time():
    print("I couldn't hack your password in less than 60sec!")
    print()
    print("Unfortunately hackers might have faster computer, I think we should check how secure it is!")
    print()



healthcheck = input("Do you want to check how safe your password is? yes/no ")


if healthcheck == "yes":

    new_password = input("Think of better password and let\'s check it! Your new password: ")
    print()
    lowercase = 0
    uppercase = 0
    punctuation = 0
    numbers = 0

    #to check improvement of password
    check_character_number = "missing"
    check_uppercase = "missing"
    check_numbers = "missing"
    check_punctuation = "missing"

    while check_character_number == "missing" or check_numbers == "missing" or check_punctuation == "missing" or check_uppercase == "missing":
        character_number = len(new_password)

        for char in new_password:

            # uppercase count
            if char in string.ascii_uppercase:
                uppercase = + 1

            # punctuation count
            elif char in string.punctuation:
                punctuation = + 1

            # numbers count
            elif char in string.digits:
                numbers = + 1

        # password healthcheck output
        print("****************************")
        print("*** PASSWORD HEALTHCHECK ***")
        print("****************************")
        print()
        print(f"Your password \"{new_password}\" has {character_number} characters.")
        print()

        if character_number < 12:
            print("</3 It's too short. It should consist minimum of 12 characters. <--- ADD CHARACTERS")
            print()
            check_character_number = "missing"

        else:
            print("<3 Well done! The length of your password is sufficient.")
            print()
            check_character_number = "good"

        if uppercase == 0:
            print("</3 Ups! No uppercase characters! Your password should have at least one. <--- ADD CAPITAL LETTER")
            print()
            check_uppercase = "missing"

        else:
            print("<3 Good job! One or more uppercase characters makes your password more secure.")
            print()
            check_uppercase = "good"

        if numbers == 0:
            print("</3 Ups! You didn't include any numbers. At least one number in your password will keep you safer. <--- ADD NUMBER")
            print()
            check_numbers = "missing"

        else:
            print("<3 Woooohooo! You have one or more digits there. Keep these numbers in your password, no hacker will crack it!")
            print()
            check_numbers = "good"

        if punctuation == 0:
            print("</3 You need some punctuation marks in your password. Make it shine! <--- ADD SPECIAL CHARACTER")
            print()
            check_punctuation = "missing"

        else:
            print("<3 Lovely! Your password contains punctuation marks. You made it real safe!")
            print()
            print("****************************")
            check_punctuation = "good"
            print()

        if check_character_number == "missing" or check_numbers == "missing" or check_punctuation == "missing" or check_uppercase == "missing":
            print()
            new_password = input("Unfortunately your password is not safe! Have a look at healthcheck report and try again: ")

        else:
            break

# SAFE password algorythm
# User input: Do you want to generate safer password?
print()
print("Your password is safe now! No cracker will hack it! Ups.. No hacker will crack it!")
print()
print("To make your password super unique and safe, you can use my password mixing algorythm.")
print()
print("National Cyber Security Centre advises to include 3 words in your password.")
print()
print("Let's choose 3 words. You can type in name of your pet, your favourite food, favourite music genre,")
print("favourite colour, first country you travelled to... Type in 3 words with spaces inbetween.")

#*** percentage of how safe password is

three_words = input("For example: franklin yellow blues. Your turn: ")

#generate 2 random indexes
random_index = list(range(len(three_words)))
random_choice1 = random.choice(random_index)
random_choice2 = random.choice(random_index)


#while loop to make sure that none of the random indexes is a space
while three_words[random_choice1] == " " or three_words[random_choice2] == " ":
    random_index = list(range(len(three_words)))
    random_choice1 = random.choice(random_index)
    random_choice2 = random.choice(random_index)

else:
    three_words = three_words.replace(three_words[random_choice1], three_words[random_choice1].upper(), 1)
    three_words = three_words.replace(three_words[random_choice2], three_words[random_choice2].upper(), 1)

#split into list
three_words = three_words.split()

#generate 2 random numbers and appends to list
random_number = random.choice(string.digits)
three_words.append(random_number)

#generate 1 random punctuation mark and appends to list
random_punctuation = random.choice(string.punctuation)
three_words.append(random_punctuation)

#shuffling list at random
random.shuffle(three_words)

#connecting list into one worded string
three_words = "".join(three_words)

print(f"Your new password is: {three_words}")

# replacing common characters with punctuation or numbers algorithm
hard_password = input("Would you like to make it even harder to hack? yes/no ")

if hard_password == "yes":
    three_words = three_words.replace("o", "0")
    three_words = three_words.replace("s", "$")
    three_words = three_words.replace("i", "1")
    three_words = three_words.replace("a", "4")
    three_words = three_words.replace("b", "8")
    print(f"Your new password is: {three_words}")

else:
    print("No worries!")


#library which allows to copy text into clipboard
copy_password = input("Would you like it to be copied to your clipboard? yes/no ")

import pyperclip
if copy_password == "yes":
    pyperclip.copy(three_words)
else:
    print("No worries!")




