def do_twice(funcao1, valor):
    funcao1(valor)
    funcao1(valor)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(funcao1, valor):
    do_twice(funcao1, valor)

do_twice(print, 'spam')
print('')
do_four(print, 'spam')