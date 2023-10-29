from turtle import Turtle, Screen
import time
import random
import turtle

# Setting up screen.

level = 1
turtle.colormode(255)

screen = Screen()
screen.setup(width = 600, height = 600)
screen.listen()
screen.tracer(0)

# Initializing player class


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-270)
        self.setheading(90)

    def go_forward(self):
        self.forward(10)
        
    def go_backward(self):
        self.backward(10)

# Initializing level class


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,260)
        self.hideturtle()
        self.write(f"Level: {level}", False, "left", ("Arial", 16, "normal"))

    def level_go_up(self):
        global level
        level += 1
        self.clear()
        self.write(f"Level: {level}", False, "left", ("Arial", 16, "normal"))

# Initializing car class


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()

    def random_color(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.random_colour = (self.r, self.g, self.b)
        return self.random_colour

    def create_cars(self):
            self.shape("square")
            self.penup()
            self.goto(random.randint(0,20000),random.randint(-230,300))
            self.color(self.random_color())
            self.shapesize(stretch_wid=None, stretch_len=2)


turtle = Player()

screen.onkeypress(key = "Up", fun = turtle.go_forward)
screen.onkeypress(key = "Down", fun = turtle.go_backward)

level_up = Level()
lst = []

for _ in range(300):
     car = Car()
     lst.append(car)


def move_cars():
    for car in lst:
         car.backward(10)


def player_hit_car():
     for car in lst:
          if car.distance(turtle) < 20:
               return True


def game_is_over():
    game_over = Turtle()
    game_over.penup()
    game_over.hideturtle()
    game_over.write("GAME OVER", False, "left", ("Arial", 16, "normal"))


game_is_on = True

sleep = 0.1

while game_is_on:
    time.sleep(sleep)
    screen.update()
    if turtle.ycor() > 280:
        level_up.level_go_up()
        sleep *= 0.6
        turtle.goto(-0,-270)
    move_cars()
    if player_hit_car() == True:
            game_is_over()
            game_is_on = False



screen.exitonclick()