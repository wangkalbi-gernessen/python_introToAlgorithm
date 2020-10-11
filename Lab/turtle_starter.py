import turtle

screen = turtle.Screen() # making Screen object
t = turtle.Turtle()  # making Turtle object
t.shape("turtle")

def draw_triangle(length: int):

    for i in range(3):
        t.forward(length)
        t.right(90)

draw_triangle(100)

screen.exitonclick()