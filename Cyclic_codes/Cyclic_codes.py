import random

def get_random_polynomial(n):
    polynomial = n*[0]
    for i in range(n):
        polynomial[i] = (0 if random.random() < 0.5 else 1)
    return polynomial

def mod_2(pol):
    for i in range(len(pol)):
        pol[i] %=2
    return pol

def polynomial_multiplication(pol1, pol2):
    mult = [0]*(len(pol1) + len(pol2) - 1)
    for i1, c1 in enumerate(pol1):
        for i2, c2 in enumerate(pol2):
            mult[i1+i2] += c1*c2
    return mod_2(mult)

def polynomial_division(num, den):
    quotient = []
    remainder = []
    if(len(den) > len(num)):
        quotient=[0]
        remainder=num
        return quotient, remainder
    dividend = num
    divisor = den
    while len(dividend) > len(divisor):
        pass
    return quotient, remainder


if __name__ == "__main__":
    k = 4
    L = 3
    n = 2**L -1
    # u = get_random_polynomial(4)
    # print(u)
    u = [1, 0, 0, 1]

    g_D = get_random_polynomial(n - k)
    print(g_D)
    g = [1, 1, 0, 0, 1, 1, 1]

    v = polynomial_multiplication(u, g)
    print(v)

    # print(list(enumerate(u)))

    div = polynomial_division(g, u)
    print(div)