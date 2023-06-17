def is_palindromo(word):
    z = len(word) - 1
    for i in range(len(word)):
        if word[i] != word[z]:
            return
        print('i: ', word[i], ':')
        print('z: ', z)
        z = z - 1

is_palindromo('ana')