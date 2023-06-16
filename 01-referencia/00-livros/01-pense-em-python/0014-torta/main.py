import turtle
import math
pen = turtle.Turtle()


pen.pu()
pen.setx(-400)
pen.sety(300)
pen.pd()


def torta(qtd_lados, raio):
    angulo_interno_total = (qtd_lados - 2) * 180
    angulo_interno_individual = angulo_interno_total / qtd_lados
    meio_angulo_interno_individual = angulo_interno_individual / 2
    giro_vertice = 180 - meio_angulo_interno_individual
    #minha solução aresta = raio * math.radians((360 / qtd_lados) / 2) * 2
    aresta = raio * math.sin(((360 / qtd_lados) / 2) * math.pi / 180) * 2 #solução correta
    giro_centro = 180 - ((180 - (360 / qtd_lados)) / 2)
    for i in range (qtd_lados):
        pen.fd(raio)
        pen.lt(giro_vertice)
        pen.fd(aresta)
        pen.lt(giro_centro)
        pen.fd(raio)
        pen.rt(180)
    pen.pu()
    pen.fd(raio*2 + 10)
    pen.pd()

torta(3, 100)
torta(4, 100)
torta(5, 100)
torta(6, 100)
pen.pu()
pen.setx(-350)
pen.sety(0)
pen.pd()
torta(7, 100)
torta(8, 100)
torta(9, 100)
torta(10, 100)

turtle.mainloop()

'''


'''

