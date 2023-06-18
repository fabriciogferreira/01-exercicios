def is_palindrome(word):
    z = len(word) - 1
    for i in range(len(word)):
        if word[i] != word[z]:
            return "This is not palindrome"
        z = z - 1
    return "This is palindrome"

print(is_palindrome('test'))
print(is_palindrome('dad')) 
