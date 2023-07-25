from sympy.ntheory import factorint
import matplotlib.pyplot as plt
import time
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def crt(x,p,m):
    factors = factorint(m)
    res = 0
    for base, exp in sorted(factors.items()):
        m_i = base**exp
        a_i = 1
        for i in range(p):
            a_i = (a_i * x) % (m_i)
        b_i = int(m/m_i)
        b_i_1 = modinv(b_i,m_i)
        res = res + a_i*b_i*b_i_1
    res = res % m
    return res
def without_crt(x,p,m):
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    # res = 1
    # for i in range(p):
    #     res = (res*x) % m
    # return res
    return (x ** p) % m
if __name__ == '__main__':
    try:
        while True:
            x,p,m = list(map(int,input("x^p mod m\ninput x,p,m").split(',')))
            start1 = time.time()
            print(without_crt(x, p, m))
            end1 = time.time()
            print(f"without CRT {end1 - start1}")
            start2 = time.time()
            print(crt(x, p, m))
            end2 = time.time()
            print(f"with CRT {end2 - start2}")
    except KeyboardInterrupt:
        pass



