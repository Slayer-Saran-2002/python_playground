# from turtle import Turtle,Screen
import turtle
import random

tup=turtle.Turtle()
tup.shape("classic")
tup.color("black")
turtle.colormode(255)
my_screen =turtle.Screen()
# print(my_screen.canvheight)
# my_screen.delay(5)
tup.speed("fastest")
# tup.pensize(10)

def random_colors():
    """Generate Random RGB colors"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) #tuple
# Square
# for i in range(4): 
#     tup.forward(100)
#     tup.right(90)
# ***********Dashed line
# for i in range(10):
#     tup.forward(10)
#     tup.penup()
#     tup.forward(10)
#     tup.pendown()
# ***********Drawing Different Shapes
# def draw_shape(num_sides):
#     for i in range(num_sides):
#         tup.forward(100)
#         tup.right(360/num_sides)

# for sides in range(3,8):
#     tup.pencolor(random_color())
#     draw_shape(sides)

# ************Random Walk
# directions= [0,90,180,270]
# for i in range(100):
#     tup.pencolor(random_colors())
#     tup.forward(20)    
#     tup.setheading(random.choice(directions))

# ************Spirograph
def spirograph(gapping):
    for i in range(int(360/gapping)):
        tup.color(random_colors())
        tup.circle(100)
        tup.setheading(tup.heading()+gapping)

spirograph(6)


my_screen.exitonclick()