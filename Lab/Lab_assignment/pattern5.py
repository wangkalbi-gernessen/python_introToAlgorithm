import turtle
import math
t = turtle.Turtle()
d = 150
def change_position(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
def draw_square2(d, x, y):
    change_position(x,y)
    t.forward(d/2)
    t.left(90)
    for _ in range(3):
        t.forward(d)
        t.left(90)
    t.forward(d/2)
for _ in range(5):
    draw_square2(d,0,0)
    t.left(360/5)
turtle.exitonclick()