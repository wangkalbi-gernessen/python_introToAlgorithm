import turtle
import math
t = turtle.Turtle()
d = 150
def change_position(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
def draw_square(d, x, y):
    change_position(x,y)
    for _ in range(4):
        t.forward(d)
        t.left(90)
draw_square(d, 0, 0)
draw_square(d, d/2, d/2)
turtle.exitonclick()