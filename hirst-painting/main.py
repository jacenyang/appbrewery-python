# import colorgram
#
# colors = colorgram.extract('image.jpg', 6)
#
# rgb_colors = []
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)

color_list = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233)]

james = turtle.Turtle()
james.hideturtle()
james.penup()
james.speed(0)

y = -225

for _ in range(10):
    james.goto(-225, y)
    for _ in range(10):
        james.dot(20, random.choice(color_list))
        james.forward(50)
    y += 50

screen = turtle.Screen()
screen.exitonclick()
