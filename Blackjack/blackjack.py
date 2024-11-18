import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
user_total = 0
for card in range(0, 2):
    user_cards.append(random.choice(cards))
user_total = sum(user_cards)
print(f"Your cards: {user_cards}, current score: ", user_total)
dealers_first_card = random.choice(cards)
print(f"Computer's first card: {dealers_first_card}")

another_card = input("Type 'y' to get another card, type 'n' to pass: ")
if another_card == "y":
    user_cards.append(random.choice(cards))
    total = sum(user_cards)
    print(f"Your cards: {user_cards}, your current score: ", total)
    print(f"Computer's first card: {dealers_first_card}, computer's current score: ", dealers_first_card)
    print(f"Your final hand: {user_cards}, your final score: ", total)
    dealers_second_card = random.choice(cards)
    dealers_total = dealers_first_card + dealers_second_card
    if dealers_total < 16:
        dealers_third_card = random.choice(cards)
        dealers_total = dealers_first_card + dealers_second_card + dealers_third_card
        print(
            f"Computer's final cards: [{dealers_first_card}, {dealers_second_card}, {dealers_third_card}], computer's current score: ",
            dealers_total)
    else:
        print(f"Computer's final cards: [{dealers_first_card}, {dealers_second_card}], computer's current score: ",
              dealers_total)

    if total < 21:
        if total > dealers_total:
            print("You win!!!")
        else:
            print("Computer wins!!!!, You lose!!")
    else:
        print("You went over. You lose!!!")

else:
    print(f"Your cards: {user_cards}, your current score: ", user_total)
    print(f"Computer's first card: {dealers_first_card}, computer's current score: ", dealers_first_card)
    print(f"Your final hand: {user_cards}, your final score: ", user_total)
    dealers_second_card = random.choice(cards)
    dealers_total = dealers_first_card + dealers_second_card
    if user_total < 21:
        print(f"Computer's final cards: [{dealers_first_card}, {dealers_second_card}], computer's final score: ",
              dealers_total)
        if user_total > dealers_total:
            print("You win!!!")
        else:
            print("Computer wins!!!!, You lose!!")
    else:
        print("You went over. You lose!!!")
