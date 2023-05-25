import turtle
bob = turtle.Turtle()
def square(pen, l):
    for i in range(4):
        pen.fd(l)
        pen.lt(90)
square(bob, 200)
turtle.mainloop()