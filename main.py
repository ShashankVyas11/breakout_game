import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color(colors[i])
    brick.shapesize(stretch_wid=1, stretch_len=5)
    brick.penup()
    brick.goto(-250, 200 - i * 25)
    bricks.append(brick)

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (ball.ycor() < brick.ycor() + 12.5 and ball.ycor() > brick.ycor() - 12.5) and (ball.xcor() > brick.xcor() - 50 and ball.xcor() < brick.xcor() + 50):
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1

    # Check if all bricks are destroyed
    if all(brick.xcor() == 1000 for brick in bricks):
        ball.goto(0, 0)
        ball.dx *= random.choice([-1, 1])
        ball.dy *= random.choice([-1, 1])
        for brick in bricks:
            brick.goto(-250, 200)

    # Game over if the ball goes below the paddle
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        for brick in bricks:
            brick.goto(-250, 200)

    # Pause to control the speed of the game
    time.sleep(0.01)