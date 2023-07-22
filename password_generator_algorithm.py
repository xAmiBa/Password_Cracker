import random
import pyperclip
import string

# PASSWORD GENERATOR ALGORYTHM
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

    # Function that uses pyperclip module to copy variable into the users' clipboard.
    def copy_password_to_clipboard(copy_password):
        if copy_password == "yes":
            pyperclip.copy(three_words)
            print()
            print("Password copied!")
        elif copy_password == 'no':
            print()
            print("No worries!")

    # User chooses if they want to copy they newly generated password.
    copy_password = input("Would you like it to be copied to your clipboard? yes/no ")
    print()
    copy_password_to_clipboard(copy_password)

    # User chooses if they want to advance their password security with advanced generator.
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

# User chooses to not generate new password with generator algorythm
else:
    print("No worries!")

