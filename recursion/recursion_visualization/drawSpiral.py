"""
we will use the built-in turtle module to draw a spiral shape using recursion

"""
import turtle

# create a turtle object
my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def drawSpiral(turtle, len_line):
    if len_line > 0:        # when the function reaches the base case, its gonna quit
        turtle.forward(len_line)
        turtle.left(90)
        drawSpiral(turtle, len_line-5)

drawSpiral(my_turtle, 100)
my_win.exitonclick()