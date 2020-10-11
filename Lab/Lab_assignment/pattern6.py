import turtle
screen = turtle.Screen()
diego = turtle.Turtle()
diego.shape("turtle")

def draw_star(length):
    for i in range(5):
        diego.forward(length)
        diego.right(144)

draw_star(100)

screen.exitonclick()