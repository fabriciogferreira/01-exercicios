import turtle
bob = turtle.Turtle()
def poligono(pen, l, arestas):
    angulo = 360 / arestas
    for i in range(arestas):
        pen.fd(l)
        pen.rt(angulo)
poligono(bob, 200, 4)
turtle.mainloop()