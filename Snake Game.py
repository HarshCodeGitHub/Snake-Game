# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("blue")
wn.bgpic("HN2.gif")
wn.setup(width=565, height=315)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


food = turtle.Turtle()
food_shape = (
(0, 0), (-4, -2), (-6, -4), (-7, -6), (-8, -8), (-8, -12), (-6, -16), (-4, -17), (-2, -19), (0, -20), (0, -22),
(0, -24), (0, -26), (2, -19), (4, -17), (6, -16), (8, -12), (8, -8), (7, -6), (6, -4), (4, -2), (-3, -2), (-8, 2),
(-6.6, -5), (3, -2), (8, 2), (6.6, -5))
turtle.register_shape('mouse', food_shape)
food.shape('mouse')
food.color('grey')
food.speed(0)
food.penup()
food.goto(8, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 10)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 12, "bold"))


# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def stop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Bindings
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(stop, "space")

segments = []

# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 190 or head.xcor() < -190 or head.ycor() > 130 or head.ycor() < -130:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        food.shape("mouse")
        food.color("grey")
        for segment in segments:
            segment.goto(500, 500)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 12, "normal"))
    if head.distance(food) < 20:
        x = random.randint(-180, 180)
        y = random.randint(-120, 120)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        # new_segment.speed()
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 12, "normal"))

    # segments need to move when the snakehead moves.
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            food.shape("mouse")
            food.color("grey")
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 12, "normal"))
    time.sleep(delay)

wn.mainloop()

