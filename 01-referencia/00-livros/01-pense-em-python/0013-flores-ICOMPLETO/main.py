import turtle
import math
bob = turtle.Turtle()

#Numero de petalas
#raio
#largura das petalasa

def flores(pen, qtd_petalas, raio, l_petalas):
    angulo_petala = 360 / qtd_petalas
    semi_principal = raio / 2
    semi_menor = l_petalas / 2
    perimetro = math.pi*(3*(semi_principal+semi_menor)-math.sqrt((3*semi_principal+semi_menor)*(semi_principal+3*semi_menor)))
    meio_perimetro = perimetro / 2
    arestas = meio_perimetro / 180
    for i in range(qtd_petalas):
        pen.lt(angulo_petala)
        for j in range(360):
            pen.lt(j)
            pen.fd(arestas)

flores(bob, 5, 1000, 50)