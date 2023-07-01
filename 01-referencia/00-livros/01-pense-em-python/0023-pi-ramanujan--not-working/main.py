import math

print(math.pow(396, 4 * 0))

def sum_terms():
    result_term = 0
    k = 0
    while True:
        term = (math.factorial(4 * k) + (1103 + 26390 * k)) / math.pow(math.factorial(k), 4) * math.pow(396, (4 * k))
        result_term = result_term + term
        print('Result Term | Term ', k+1, ': ', result_term, term)
        k = k + 1
        if term < 10**-15:
            break
    return result_term


aproximate = ((2 * math.sqrt(2)) / 2) + sum_terms()
print(aproximate)
print(math.pi)
print(1/math.pi)
print(10**15)
print(1>10**-15)