from turtle import Turtle, Screen

tim = Turtle("square")
screen = Screen()


def up():
    tim.setheading(90)
    tim.forward(30)


def down():
    tim.setheading(270)
    tim.forward(30)


def left():
    tim.setheading(180)
    tim.forward(30)


def right():
    tim.setheading(0)
    tim.forward(30)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.exitonclick()