import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=700, height=500)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color: ")
print(bet)

colors = ["red", "orange", "blue", "green", "yellow", "purple"]

if bet:
    is_race_on = True

x = -300.00
y = -50.00
turtles = []

for color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 30
    turtles.append(new_turtle)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 330.00:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! {winning_color} is the winner!!")
            else:
                print(f"You've lost! {winning_color} is the winner!!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
