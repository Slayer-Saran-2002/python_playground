import turtle

tup=turtle.Turtle()
tup.shape("classic")
tup.color("black")
turtle.colormode(255)
my_screen =turtle.Screen()
tup.pensize(5)

def forward():
    tup.forward(10)
def backward():
    tup.backward(10)
def left_rotate():
    tup.left(10)
def right_rotate():
    tup.right(10)
def clear():
    tup.clear()
    tup.penup()
    tup.home()
    tup.pendown()

my_screen.listen()
my_screen.onkey(key = "w",fun = forward) # keyword argument
my_screen.onkey(key = "s",fun = backward)
my_screen.onkey(key = "a",fun = left_rotate)
my_screen.onkey(key = "d",fun = right_rotate)
my_screen.onkey(clear,"c") # same as above #positional argument




my_screen.exitonclick()