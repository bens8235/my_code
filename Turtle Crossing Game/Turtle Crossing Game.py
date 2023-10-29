from turtle import Turtle, Screen
import time
import random
import turtle

# Setting up screen & turtle.

turtle.colormode(255)

screen = Screen()

screen.setup(width = 600, height = 600)
screen.listen()
screen.tracer(0)

turtle = Turtle("turtle")
turtle.color("black")
turtle.penup()
turtle.goto(0,-270)
turtle.setheading(90)

# Setting forward & backward keys.

def forward():
    turtle.forward(10)


def backward():
    turtle.backward(10)


screen.onkeypress(key = "Up", fun = forward)
screen.onkeypress(key = "Down", fun = backward)

# Setting up writing to show which level user is on.

level = 1

level_up = Turtle()
level_up.penup()
level_up.goto(-280,260)
level_up.hideturtle()

level_up.write(f"Level: {level}", False, "left", ("Arial", 16, "normal"))

def level_go_up():
    global level
    level += 1
    level_up.clear()
    level_up.write(f"Level: {level}", False, "left", ("Arial", 16, "normal"))


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour


# Created random cars to move along the screen.

lst = []
for _ in range(300):
    car = Turtle("square")
    car.penup()
    car.goto(random.randint(0,20000),random.randint(-230,300))
    car.color(random_color())
    car.shapesize(stretch_wid=None, stretch_len=2)
    lst.append(car)


def move_cars():
    for car in lst:
        car.backward(10)


def game_is_over():
    game_over = Turtle()
    game_over.penup()
    game_over.hideturtle()
    game_over.write("GAME OVER", False, "left", ("Arial", 16, "normal"))


game_is_on = True
sleep = 0.1

# If turtle reaches top of screen, level goes up and program runs faster, turtle reset. Move cars and detect collision.

while game_is_on:
    time.sleep(sleep)
    screen.update()
    if turtle.ycor() > 280:
        level_go_up()
        sleep *= 0.6
        turtle.goto(-0,-270)
    move_cars()
    for car in lst:
        if car.distance(turtle) < 20:
            game_is_over()
            game_is_on = False

screen.exitonclick()