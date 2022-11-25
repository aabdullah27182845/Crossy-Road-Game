from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for i in range(100):
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.initial_position = (random.randint(300, 350), random.randint(-230, 230))
            car.random_position = (random.randint(-240, 300), random.randint(-230, 230))
            car.goto(car.random_position)
            car.hideturtle()
            self.cars.append(car)

    def show_cars(self, level):
        for i in range(10 + 5 * level):
            self.cars[i].showturtle()

    def increment_level(self):
        self.car_speed += MOVE_INCREMENT
        for i in range(len(self.cars)):
            self.cars[i].goto(self.cars[i].random_position)

    def move_cars(self, level):
        for i in range(10 + 5 * level):
            if self.cars[i].xcor() > -350:
                self.cars[i].goto(x=self.cars[i].xcor() - self.car_speed, y=self.cars[i].ycor())
            else:
                self.cars[i].goto(self.cars[i].initial_position)
