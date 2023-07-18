import string
import random

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


