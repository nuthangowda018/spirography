import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
tim=Turtle()
tim.speed(9)


def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rc = (r, g, b)
    return rc
i=0
for _ in range(36):
    tim.color(colour())
    tim.circle(100)
    tim.setheading(i)
    i+=20










screen=Screen()
screen.exitonclick()