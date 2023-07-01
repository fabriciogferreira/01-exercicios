import math

def test_square_root(rooting, root):
    print("Rooting | My Root | Math Root | Diff", )
    print(rooting, " | ", root, " | ",  math.sqrt(rooting), " | ",  math.sqrt(rooting) - root)

def my_square_root(rooting):
    while True:
        number_random = float(input("Write a number plus than 0: "))
        if number_random > 0:
            break
    while True:
        root = (number_random + rooting / number_random) / 2
        print("Rooting: ", rooting, "; Random: ", number_random)
        if root == number_random:
            break
        number_random = root
    test_square_root(rooting, root)
my_square_root(4)
