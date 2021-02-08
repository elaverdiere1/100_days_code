#Password Generator Project
import random

# possible letters, symbols, and numbers

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# user inputs

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# building the list based in user input

start_password = []
for x in range(nr_letters):
  start_password.append(random.choice(letters))
for y in range(nr_symbols):
  start_password.append(random.choice(symbols))
for z in range(nr_numbers):
  start_password.append(random.choice(numbers))

# randomizing for the final password

final_password = random.sample(start_password, len(start_password))

# returning the answer as a string

password_string = ''.join(map(str,final_password))
print(password_string)
