import turtle
import os
import platform

wn = turtle.Screen()
wn.title('pong by Daniil_Dn')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=2, stretch_len=2)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align='center', font=("Courier", 24, "normal"))


# Functions

def play_sound(file_name):
    platform_sys = platform.system()
    if platform_sys == "Linux":
        os.system(f"aplay {file_name}&")
    elif platform_sys == "Darwin":
        os.system(f"afplay {file_name}&")
    elif platform_sys == "Windows":
        import winsound
        winsound.PlaySound(file_name, winsound.SND_ASYNC)


def paddle_a_up() -> None:
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down() -> None:
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up() -> None:
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down() -> None:
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    try:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            play_sound('b.wav')

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            play_sound('b.wav')

        if ball.xcor() > 390:
            score_a += 1
            pen.clear()
            pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            play_sound('b.wav')
        if ball.xcor() < -390:
            score_b += 1
            pen.clear()
            pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            play_sound('b.wav')

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            play_sound('b.wav')

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            play_sound('b.wav')

    except Exception as error:
        print('smth went wrong: \n', error)
        break
