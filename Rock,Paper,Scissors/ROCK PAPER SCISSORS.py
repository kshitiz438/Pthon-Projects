# ROCK PAPER SCISSORS


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_throws = int(input("Type 0 for rock, 1 for paper and 2 for scissors:\n "))
if user_throws == 0:
    print(rock)
elif user_throws == 1:
    print(paper)
elif user_throws == 2:
    print(scissors)

comp_throws = random.randint(0, 2)
print("The computer chose: ", comp_throws)
if comp_throws == 0:
    print(rock)
elif comp_throws == 1:
    print(paper)
elif comp_throws == 2:
    print(scissors)

if user_throws == comp_throws:
    print("It's a draw")
elif (user_throws == 0 and comp_throws == 1) or (user_throws == 1 and comp_throws == 2) or (
        user_throws == 2 and comp_throws == 0):
    print("Computer Wins")
elif (user_throws == 1 and comp_throws == 0) or (user_throws == 2 and comp_throws == 1) or (
        user_throws == 0 and comp_throws == 2):
    print("User Wins")
