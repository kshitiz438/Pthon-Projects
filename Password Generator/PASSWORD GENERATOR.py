import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '<', '>', '?']
print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letter would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in you password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
l = ''
n = ''
s = ''
for i in range(nr_letters):
    l = l + random.choice(letters)
for j in range(nr_numbers):
    n = n + random.choice(numbers)
for k in range(nr_symbols):
    s = s + random.choice(symbols)
password = list(l + n + s)
random.shuffle(password)
hard_password = ''.join(password)
print("Here is your Password: " + hard_password)
