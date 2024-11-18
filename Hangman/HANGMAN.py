import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
no_of_stages = len(stages)
print("You have ", no_of_stages, " lives")

word_list = ["inferno", "dexter", "flash", "aviator"]
word = random.choice(word_list)

display = []
length = len(word)
for i in range(length):
    display.append("_")
print(display)

no_of_lives = 0
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    if guess not in word:
        print(stages[no_of_lives])
        no_of_lives += 1
        print("You have ", (no_of_stages - no_of_lives), " lives left")
    print(display)
    if (no_of_stages == no_of_lives) or ("_" not in display):
        end_of_game = True

if no_of_lives == no_of_stages:
    print("You have lost!!!")
else:
    print("You have won!!!")
