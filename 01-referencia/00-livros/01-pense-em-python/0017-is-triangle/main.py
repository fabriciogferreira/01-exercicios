def is_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        print('This can make a triangle')
        if a + b == c or b + c == a or c + a == b:
            print('This a triangle degenerate.')
    else:
        print('This can not make a triangle')
            
def input_sides_triangle():
    a = int(input('Write the side a: ')) 
    b = int(input('Write the side b: '))
    c = int(input('Write the side c: '))
    is_triangle(a, b, c)

input_sides_triangle()
