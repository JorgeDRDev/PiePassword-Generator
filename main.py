import random
from chara import uppercase_letters, lowercase_letters, special_characters, numbers

password = []
print("Welcome to the PiePassword Generator!")
letter_amt = int(input("How many letters would you like in your password? "))
if letter_amt % 2 == 0:
    letter_amt = round(letter_amt / 2)
    for x in range(letter_amt):
        password.append(random.choice(uppercase_letters))
    for x in range(letter_amt):
        password.append(random.choice(lowercase_letters))
else:
    for x in range(letter_amt):
        password.append(random.choice(lowercase_letters))
special_characters_amt = int(input("How many symbols would you like? "))
for x in range(special_characters_amt):
    password.append(random.choice(special_characters))
numbers_amt = int(input("How many numbers would you like? "))
for x in range(numbers_amt):
    password.append(random.choice(numbers))
random.shuffle(password)
print("Here is your password: " + "".join(password))
