import turtle
bob = turtle.Turtle()
def square(pen, l, arestas):
    angulo = 360 / arestas
    for i in range(arestas):
        pen.fd(l)
        pen.lt(angulo)
square(bob, 200, 7)
turtle.mainloop()