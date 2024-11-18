from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Gadugi", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 320)
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def scorecard(self):
        self.clear()
        self.score += 1
        self.update_scorecard()
