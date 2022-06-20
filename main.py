import turtle as t
import colorgram
import random


t.colormode(255)
tt = t.Turtle()
def set_position():
    tt.up()
    tt.sety(-100)
    tt.setx(-250)
    tt.down()

colors = colorgram.extract('image.jpeg',50)
color_list = []
for i in range(len(colors)):
    clr = colors[i]
    color_list.append((clr.rgb[0],clr.rgb[1],clr.rgb[2]))
# color_list = [(249, 236, 206), (28, 27, 18), (80, 100, 124), (191, 156, 127), (111, 99, 86), (134, 147, 159), (24, 28, 35), (233, 198, 135), (35, 25, 31), (18, 22, 19), (111, 99, 104), (148, 158, 152), (112, 126, 147), (148, 120, 112), (74, 73, 36), (44, 62, 94), (151, 145, 79), (160, 147, 152), (99, 107, 102), (233, 225, 228), (216, 224, 232), (110, 134, 140), (225, 233, 229), (143, 119, 126), (78, 55, 69), (80, 57, 51), (119, 133, 127), (209, 184, 178), (174, 179, 222), (205, 184, 189)]
def line():
    for i in range (10):
        tt.dot(20, random.choice(color_list))
        tt.up()
        tt.fd(50)
        tt.down()

def next_line():
    tt.up()
    tt.setheading(180)
    tt.forward(500)
    tt.setheading(90)
    tt.forward(50)
    tt.setheading(0)


set_position()
for i in range(10):
    line()
    next_line()

screen = t.Screen()
screen.exitonclick()