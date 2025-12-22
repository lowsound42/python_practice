# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_characters_in_password = nr_letters + nr_symbols + nr_numbers

# pick our random letters
selected_letters = []
for i in range(nr_letters):
    selected_letters.append(random.choice(letters))

# pick our random symbols
selected_symbols = []
for i in range(nr_symbols):
    selected_symbols.append(random.choice(symbols))

# pick our random sybols
selected_numbers = []
for i in range(nr_numbers):
    selected_numbers.append(random.choice(numbers))

selected_characters = selected_letters + selected_symbols + selected_numbers

random.shuffle(selected_characters)

for i in selected_characters:
    password += i
print(password)
