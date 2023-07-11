abc = 'abcdefghijklmnopqrstuvwxyz'

def index(letter):
    if letter == 'a':
        return 0
    j = 0
    while letter != abc[j]:
        j = j + 1
    return j

def rotate_word(word, rotate):
    frase = ''
    for i in range(len(word)):
        new_index = rotate + index(word[i])
        while new_index < 0 or new_index > len(abc) - 1:
            if new_index > len(abc):
                new_index = new_index - len(abc)
            else:
                new_index = new_index + len(abc)
        frase = frase + abc[new_index]
    return frase
        

print(rotate_word('ibm', -1))