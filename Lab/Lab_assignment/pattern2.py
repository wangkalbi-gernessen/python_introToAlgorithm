import turtle
screen = turtle.Screen()
diego = turtle.Turtle()
diego.shape("turtle")

def draw_square(length):
    for i in range(4):
        diego.forward(length)
        diego.right(90)

    diego.penup()
    diego.goto(90,45)
    diego.pendown()
    diego.right(45)

    for i in range(4):
        diego.forward(length)
        diego.right(90)

draw_square(200)


screen.exitonclick()