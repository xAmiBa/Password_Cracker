# Password Security Python Program

This Python program is designed to perform several functions related to password security. It consists of multiple steps and functionalities that help the user check the strength of their password, generate a new strong password, and enhance its security using custom hashing techniques.

## Functionality Overview:

1. **Brute Force Attack Simulation:**
   - The program simulates a brute force attack on a user-input password.
   - It generates random passwords of the same length as the user's input password and compares them.
   - The loop continues until either the correct password is guessed or a time limit of 60 seconds is reached.
   - If the correct password is cracked within 60 seconds, the program informs the user, displaying the time taken and the number of attempts made.
   - If the time limit is exceeded, the program notifies the user that the password was not cracked.

2. **Password Security Level Check:**
   - The user is given the option to check the security level of their password.
   - If the user chooses "yes," they are prompted to input a new password for evaluation.
   - The program then checks the security of the new password based on specific criteria, including length, presence of uppercase characters, numbers, and punctuation marks.
   - The user is given feedback on the password's security level and safety tips to improve it.
   - The user is asked to enter a new password based on the provided feedback until the password meets the security criteria.

3. **Password Generation with custom hashing algorithm:**
   - The program offers the user the option to generate a brand new password using the "Password Mixer" algorithm.
   - The user is instructed to input three random words separated by spaces.
   - Two random words are then converted to uppercase characters.
   - A random digit and punctuation mark are appended to the password.
   - The list of words and characters is shuffled to create a unique password.
   - The user can choose to further enhance the password's security using advanced hashing techniques.
   - Specific characters in the password are replaced with numeric or punctuation counterparts.
   - The user has the option to copy the modified password to their clipboard.

## Libraries Used:

- `random`: For generating random passwords, indexes, and choices.
- `string`: For accessing pre-defined sets of characters like lowercase letters, uppercase letters, digits, and punctuation marks.
- `time`: For measuring the time taken for password cracking and setting a timeout for the brute force attack.
- `pyperclip`: For copying the generated password to the user's clipboard.
