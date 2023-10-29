from turtle import Screen, Turtle
import time

# Setting up screen

screen = Screen()
screen.setup(width = 800,height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()

# Setting up paddles.

class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.goto(coordinate)
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=None, stretch_len=5)

    def goup(self):
        self.forward(30)

    def godown(self):
        self.backward(30)

# Setting up ball

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

# Setting up scoreboard


class ScoreBoard(Turtle):
     def __init__(self):
        super().__init__()
        self.scoreL = 0
        self.scoreR = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        
        
     def draw(self):
        self.penup()
        self.goto(-80,200)
        self.write(self.scoreL,"center", font = ("Verdana", 50, "normal"))
        self.goto(40,200)
        self.write(self.scoreR,"center", font = ("Verdana", 50, "normal"))
        self.goto(0,300)
        self.pendown()
        self.setheading(270)
        for i in range(50):
            self.forward(10)
            self.penup()
            self.forward(5)
            self.pendown()
         

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()
scoreboard.draw()


screen.onkeypress(key = "Up", fun = r_paddle.goup)
screen.onkeypress(key = "Down", fun = r_paddle.godown)
screen.onkeypress(key = "w", fun = l_paddle.goup)
screen.onkeypress(key = "s", fun = l_paddle.godown)

game_is_on = True
sleep = 0.1
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep *= 0.8


    if ball.xcor() > 400:
        ball.goto(0,0)
        sleep = 0.1
        ball.bounce_x()
        scoreboard.clear()
        scoreboard.scoreL += 1
        scoreboard.draw()
        
    if ball.xcor() <-400:
        ball.goto(0,0)
        sleep = 0.1
        ball.bounce_x()
        scoreboard.clear()
        scoreboard.scoreR += 1
        scoreboard.draw()
        
screen.exitonclick()

