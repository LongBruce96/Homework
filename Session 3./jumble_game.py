#3.1

import random
word = "champion"
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(jumble)
guess = input("Your answer: ")
if guess != correct and guess != "":
    print(":(")
if guess == correct:
    print("Hura")

# 3.2

import random
WORDS = ("meticulous", "champion", "hexagon",)
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(jumble)
guess = input("Your answer: ")
if guess != correct and guess != "":
    print(":(")
if guess == correct:
    print("Hura")