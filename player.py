from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.y_pos = -280
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.y_pos += MOVE_DISTANCE
        self.goto(x=0, y=self.y_pos)

    def down(self):
        self.y_pos -= MOVE_DISTANCE
        self.goto(x=0, y=self.y_pos)

    def reset_position(self):
        self.y_pos = -280
        self.goto(x=0, y=self.y_pos)
