while True:
    comand = input('Write some valid: ')
    if comand == 'done':
        print('Bye bye')
        break
    print(eval(comand))