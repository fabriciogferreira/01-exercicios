import turtle
import math
bob = turtle.Turtle()

#Minha versão
import turtle
bob = turtle.Turtle()
def square(pen, raio):
    circunferencia = 2*math.pi*raio
    arestas = circunferencia / 360
    for i in range(360):
        pen.fd(arestas)
        pen.lt(1)
square(bob, 100)
turtle.mainloop()

#manda o bob, manda raio
# angulo = circunferencia / 360

#Resposta
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
#circle(bob, 50)
