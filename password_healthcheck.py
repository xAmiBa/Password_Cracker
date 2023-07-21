import string

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

