import turtle
from shutil import move
from turtle import Turtle, Screen
import random
turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

tt = Turtle()
tt.speed('fastest')

direction = [0, 90, 180, 270]

# for i in range(3,11):
#     tt.color(random_colour())
#     angle = 360/i
#     for _ in range(i):
#         tt.forward(100)
#         tt.right(angle)

# for i in range(200):
#     tt.color(random_colour())
#     tt.setheading(random.choice(direction))
#     tt.forward(30)

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tt.color(random_colour())
        tt.circle(100)
        tt.setheading(tt.heading() + size_of_gap)

for _ in range(10):
    spirograph(5)
    tt.forward(10)
    spirograph(5)
screen = Screen()
screen.exitonclick()