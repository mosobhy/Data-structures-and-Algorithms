"""
we are going to draw a fractal tree using a recursvie algorithm

fractl shapes: are the shapes that look the same at any level of maginfication 
"""

import turtle

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)   # to get the place we started over before turning right + 20 degree
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

if __name__ == "__main__":
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('blue')
    tree(75, t)
    my_win.exitonclick()
