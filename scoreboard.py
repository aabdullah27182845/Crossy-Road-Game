from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(x=-200, y=240)
        self.level = 0
        self.game_delay = 0.1
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.game_delay *= 0.75
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        return self.level

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
