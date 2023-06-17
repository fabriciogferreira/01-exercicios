mensage = 'Hello World!'
qtd_rept = 900

def rept_mensage(mensage, qtd_rept):
    if qtd_rept <= 0:
        return
    print(mensage)
    rept_mensage(mensage, qtd_rept - 1)

rept_mensage(mensage, qtd_rept)