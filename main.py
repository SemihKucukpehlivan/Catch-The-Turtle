import turtle
import random
import time

# Screen
drawing_screen = turtle.Screen()
drawing_screen.bgcolor("light blue")

score = 0

start_time = time.time()
countdown_time = 10

last_click_time = time.time()
time_limit = 2

#score board
score_board = turtle.Turtle()
score_board.color("blue")
# no line visible
score_board.penup()
score_board.hideturtle()
# where the score will appear on the screen
score_board.goto(0, 250)
score_board.write(f"Score: {score}", font=("Courier", 25, "normal"),align="center",)

#countdown
countdown = turtle.Turtle()
countdown.color("black")
countdown.penup()
countdown.hideturtle()
countdown.goto(0, 200)

# create turtle
drawing_turtle = turtle.Turtle()
drawing_turtle.shape("turtle")
drawing_turtle.color("green")
drawing_turtle.penup()
# to move randomly
drawing_turtle.goto(random.randint(-150, 150), random.randint(-150, 150))


def clicked(x, y):
    global last_click_time, score, time_off
    current_time = time.time()
    if current_time - last_click_time <= time_limit:
        score += 1
        score_board.clear()
        score_board.write("Skor: {}".format(score), align="center", font=("Courier", 25, "normal"))
        drawing_turtle.goto(random.randint(-280, 280), random.randint(-280, 280))
    last_click_time = current_time


drawing_screen.onclick(clicked)

while True:
    current_time = time.time()
    elapsed_time = countdown_time - int(current_time - start_time)
    if current_time - last_click_time > time_limit:
        drawing_turtle.goto(random.randint(-280, 280), random.randint(-280, 280))
        last_click_time = current_time

    elif elapsed_time <= 0:
        countdown.clear()
        countdown.write("Game Over!!", align="center", font=("Courier", 24, "normal"))
        break
    else:
        countdown.clear()
        countdown.write("Time:{}".format(int(elapsed_time)), align="center", font=("Courier", 24, "normal"))
    time.sleep(1)

    drawing_screen.update()

