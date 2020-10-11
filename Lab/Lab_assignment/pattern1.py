import turtle
t = turtle.Turtle()
d = 100
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
draw_square(d + 100, -50, -50)
turtle.exitonclick()