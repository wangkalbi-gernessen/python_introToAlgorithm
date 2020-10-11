# patter 7 coded by Takayuki and Kazu

import turtle
import math

# Initializing
wn = turtle.Screen()
d1 = 100
d2 = 15
wn.bgcolor("#90ef8f")


# functions
def change_position(t, x, y):
    """
    Set the turtle's position without drawing
    :param t:turtle
    :param x:position_x
    :param y:position_y
    :return:
    """
    t.penup()
    t.setposition(x, y)
    t.pendown()


def draw_turtle():
    """
    creating a default turtle   :turtle >
    :return: turtle object
    """
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    return t


def draw_stright_turtle(t):
    """
    Draw turtle from center to circle :------==--turtle >
    :param t: turtle
    :return:
    """

    #position in center
    change_position(t, 0, 0)

    #move center to circle
    t.penup()
    t.forward(d1)
    t.pendown()

    #draw a short line
    t.forward(d2)
    t.penup()
    t.forward(d2)
    t.pendown()





# main

# Draw turtle in the middle
draw_turtle()


# Draw turtles around the circle
for i in range(12):
    t = draw_turtle()
    t.width(4)
    t.left(30*i)
    draw_stright_turtle(t)


turtle.exitonclick()
