import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# # Challenge 1
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Challenge 2
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# # Challenge 3
# for sides in range(3, 11):
#     tim.color(random_color())
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)

# # Challenge 4
#
# tim.pensize(15)
# tim.speed(0)
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Challenge 5
tim.speed(0)


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
