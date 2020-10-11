import turtle
screen = turtle.Screen()
diego = turtle.Turtle()
diego.shape("turtle")

def draw_all_triangles(length):
    for i in range(6):
        for j in range(3):
            diego.forward(length)
            diego.left(120)





draw_triangle(100)







# def draw_triangle(length):
#     for i in range(2):
#         for j in range(3):
#             diego.forward(length)
#             diego.left(120)
#
#         for k in range(3):
#             diego.forward(length)
#             diego.right(120)
#
#
#         diego.penup()
#         diego.goto(100, 0)
#         diego.pendown()
#
#     diego.left(60)
#     diego.forward(length)
#     diego.left(120)
#
#     for g in range(1):
#         diego.forward(length)
#         diego.left(120)
#         diego.forward(200)
#         diego.right(120)
#         diego.forward(100)
#
# draw_triangle(100)

screen.exitonclick()