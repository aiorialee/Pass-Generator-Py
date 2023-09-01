# Name: Jing Li
# Date: 01/09/2023
# Purpose: To create random password based on the # of letters, symbols and nums

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Prevent Hackers from stealing your passwords! Welcome to the password generator app.")
num_of_letters = int(input("How many letters of characters would you like?\n"))
num_of_symbols = int(input(f"How many symbols of characters would you like?\n"))
num_of_nums = int(input(f"How many numbers of characters would you like?\n"))

password_list = []

for char in range(1, num_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, num_of_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, num_of_nums + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
