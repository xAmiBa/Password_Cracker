# Import random library to create random data needed in the program.
import random
# Import string library to save time on writing character, digits and punctuation strings.
import string
# Import time library to measure password cracking time and implement timeout break.
import time
# Pyperclip library allows to copy text into users' clipboard.
import pyperclip

# FIRST STEP: BRUTE FORCE ATTACK

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


# STEP 2: CHECK PASSWORD SECURITY LEVEL

# User chooses if they want to check security of their password
healthcheck = input("Do you want to check how safe your password is? yes/no ")

# If statement starting password healthcheck if user inputs "yes"
if healthcheck == "yes":
    # User inputs new password to check its security
    new_password = input("Think of better password and let\'s check it! Your new password: ")
    print()

    lowercase = 0  # Number of lowercase characters.
    uppercase = 0  # Number of uppercase characters.
    punctuation = 0  # Number of punctuation marks.
    numbers = 0  # Number of digits.

    # Variables describing state of password security check.
    # If check is positive == "good", if check is negative == "missing" (default).
    check_character_number = "missing"
    check_uppercase = "missing"
    check_numbers = "missing"
    check_punctuation = "missing"

    """
    This while loop is repeating a block of code which checks the security of user's password.
    The loop continues while character, digit, punctuation mark or upper case character number is not
    satisfactory (any variable == "missing").
    The while loop:
    - uses if statement inside for loop to count number of different types of characters in the password
    - uses if statements to check if there is enough of different types of characters
    - assigns the "missing" or "good" value to check_variables
    - prints password healthcheck report with safety tips for the user
    - asks user for another password changed accordingly to given feedback
    The while loop terminates when user's password is safe and all check_variables == "good".
    """

    while check_character_number == "missing" \
            or check_numbers == "missing" \
            or check_punctuation == "missing" \
            or check_uppercase == "missing":

        character_number = len(new_password)  # Length of new passwort.

        for character in new_password:
            if character in string.ascii_uppercase:  # Digits characters count.
                uppercase = + 1
            elif character in string.punctuation:  # Punctuation marks count.
                punctuation = + 1
            elif character in string.digits:  # Digits characters count.
                numbers = + 1

        # Password healthcheck report for the user.
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *")
        print("P A S S W O R D    H E A L T H C H E C K    R E P O R T")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *")
        print()
        print(f"Your password \"{new_password}\" has {character_number} characters.")
        print()

        if character_number < 12:
            print("( ͡ಠ ʖ̯ ͡ಠ) It's too short. It should consist minimum of 12 characters. <--- ADD CHARACTERS")
            print()
            check_character_number = "missing"
        else:
            print("Well done! The length of your password is sufficient.")
            print()
            check_character_number = "good"

        if uppercase == 0:
            print("( ͡ಠ ʖ̯ ͡ಠ) No uppercase characters! Your password should have at least one. <--- ADD CAPITAL LETTER")
            print()
            check_uppercase = "missing"
        else:
            print("Good job! One or more uppercase characters makes your password more secure.")
            print()
            check_uppercase = "good"

        if numbers == 0:
            print("( ͡ಠ ʖ̯ ͡ಠ) Ups! You didn't include any numbers. <--- ADD NUMBER")
            print()
            check_numbers = "missing"
        else:
            print("Woooohooo! You have one or more digits there. Keep these numbers in your password,")
            print()
            check_numbers = "good"

        if punctuation == 0:
            print("( ͡ಠ ʖ̯ ͡ಠ) You need some punctuation marks. Make it shine! <--- ADD SPECIAL CHARACTER")
            print()
            check_punctuation = "missing"
        else:
            print("Lovely! Your password contains punctuation marks. You made it real safe!")
            print()
            check_punctuation = "good"
            print()

        if check_character_number == "missing" or check_numbers == "missing" or check_punctuation == "missing" or check_uppercase == "missing":
            print()
            new_password = input(
                "Unfortunately your password is not safe! Have a look at healthcheck report and try again: ")
        else:
            print("Your password is 100% safe now! No cracker will hack it! Ups.. No hacker will crack it!")
            print()
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *")

# If statement output if user does not want a password healthcheck.
else:
    print()
    print("No worries!")
    print()
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *")


# STEP 3: PASSWORD HASHING ALGORYTHM PART 1 - RANDOM "PASSWORD MIXER"
# User chooses if they want to generate new password.

password_mixer = input("Would you like to generate a brand new password with \"Password mixer\" program?: yes/no ")
print()

if password_mixer == "yes":
    # Information for the user and input request.
    print("National Cyber Security Centre advises to include 3 random words in your password.")
    print()
    print("Let's choose 3 words. You can type in name of your pet, your favourite food, favourite music genre,")
    print("favourite colour, first country you travelled to, anything you imagine...")
    print()
    three_words = input("Type in 3 words with spaces inbetween. For example: franklin yellow blues. Your turn: ")
    print()

    # Generate 2 random indexes to turn the lowercase into uppercase characters.
    random_index = list(range(len(three_words)))
    random_choice1 = random.choice(random_index)  # First random index.
    random_choice2 = random.choice(random_index)  # Second random index.

    """
    This while loop makes sure that none of the generated random indexes is a space.
    If generated random index corresponds to blank space in user input, it is generated again.
    The while loop terminates when both random indexes corresponds to characters.
    Else statement replaces lowercase letter in randomly generated index with uppercase letter.
    """

    while three_words[random_choice1] == " " or three_words[random_choice2] == " ":
        random_index = list(range(len(three_words)))
        random_choice1 = random.choice(random_index)
        random_choice2 = random.choice(random_index)

    else:
        three_words = three_words.replace(three_words[random_choice1], three_words[random_choice1].upper(), 1)
        three_words = three_words.replace(three_words[random_choice2], three_words[random_choice2].upper(), 1)

    # User input split into list. Generate random number and append it to the list.
    three_words = three_words.split()
    random_number = random.choice(string.digits)
    three_words.append(random_number)

    # Generate random punctuation mark and append it to the list.
    random_punctuation = random.choice(string.punctuation)
    three_words.append(random_punctuation)

    # Shuffle list at random and join items into one string.
    random.shuffle(three_words)
    three_words = "".join(three_words)

    print(f"Your new password is: {three_words}")
    print()

    # Function that uses pyperclip library to copy variable into the users' clipboard.
    def copy_password_to_clipboard(copy_password):
        if copy_password == "yes":
            pyperclip.copy(three_words)
            print()
            print("Password copied!")
        elif copy_password == 'no':
            print()
            print("No worries!")

    # User chooses if they want to copy their newly generated password.
    copy_password = input("Would you like it to be copied to your clipboard? yes/no ")
    print()
    copy_password_to_clipboard(copy_password)


    # STEP 3.2: PASSWORD HASHING ALGORYTHM PART 2 - ADVANCED HASHING

    # User chooses if they want to advance their password security with advanced hashing.
    print()
    hard_password = input("Would you like to make it even harder to hack? yes/no ")
    print()

    # Specific character in the password are replaced with numeric or punctuation counterparts.
    if hard_password == "yes":
        three_words = three_words.replace("o", "0")
        three_words = three_words.replace("s", "$")
        three_words = three_words.replace("i", "1")
        three_words = three_words.replace("a", "4")
        three_words = three_words.replace("b", "8")

        print(f"Your new password is: {three_words}")
        print()

        # User chooses if they want to copy they newly generated password.
        copy_password = input("Would you like it to be copied to your clipboard? yes/no ")
        copy_password_to_clipboard(copy_password)

# User chooses to not generate new password with hashing algorythm
else:
    print("No worries!")
