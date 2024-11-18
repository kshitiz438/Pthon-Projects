print('''
*******************************************************************************
|                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the Treasure")
print("Your are at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right' \n")
if direction == "left":
    print("You came to a lake, there is an Island in the middle of the lake.")
    command = input("Type 'wait' to wait for a boat, type 'swim' to swim across \n")
    if command == "wait":
        print(
            "You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        door = input("Which colour do you choose?\n")
        if door == "red":
            print("There was a fire in the house, you died as soon as you opened the door.")

        elif door == "yellow":
            print("You have found the Treasure.")
            print("YOU WIN!!!!!!")
        elif door == "blue":
            print("A pack of trolls has killed you.")

    else:
        print("Sharks have eaten you. You have died.")

else:
    print("You fell into a ditch. You have died.")
print("GAME OVER")
