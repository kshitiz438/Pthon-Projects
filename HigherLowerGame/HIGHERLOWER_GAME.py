import random
from HIGHERLOWER_ART import logo, vs
from GAMEDATA import data
from replit import clear


def format(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


is_correct = True
count = 0
choice_a = random.choice(data)

while is_correct:
    choice_b = random.choice(data)
    print(logo)
    print(f"Compare A: {format(choice_a)}")
    print(vs)
    print(f"Against B: {format(choice_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct == True:
        choice_a = choice_b
        count += 1
        clear()
        print(f"You're Right!! Current score: {count}")
    else:
        print(f"Sorry you're wrong!! Final Score: {count}")
