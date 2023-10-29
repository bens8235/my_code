from turtle import Turtle, Screen
import turtle
from random import *

# Creating user screen & asking who will win race.

screen = Screen()

answer = screen.textinput("Who will win the race? (purple, blue, green, yellow, orange or red)", "Enter a colour: ")

# creating 6 different turtle's with different colours and their starting positions.

tim = Turtle()
tom = Turtle()
tod = Turtle()
ben = Turtle()
lid = Turtle()
bob = Turtle()

lst = [tim, tom, tod, ben, lid, bob]
colours = ["purple", "blue", "green", "yellow", "orange", "red"]
initial_colour = 0
start_x = -100
start_y = 0

for name in lst:
    name.shape("turtle")
    name.penup()
    name.color(colours[initial_colour])
    initial_colour += 1
    name.goto(start_x,start_y)
    start_y += 30

# Function to choose random turtle to move forward.


def race():
    rand_name = choice(lst)
    rand_name.forward(10)

# Function to check if turtle reached the end.

def check_if_at_end():
    for name in lst:
        if name.pos()[0] >= 300:
            colour = name.color()[0]
            turtle.bye()
            if answer.lower() == colour.lower():
                print(f"You won. {colour.title()} is the winner.")
            else:
                print(f"You lose. {colour.title()} turtle is the winner.")
            return False
    return True


while check_if_at_end():
    race()





