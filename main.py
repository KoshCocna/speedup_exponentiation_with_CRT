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
    return (x ** p) % m
if __name__ == '__main__':
    # x = 12345
    # p = 67890
    # t1 = []
    # t2 = []
    # x_axis = []
    # for m in range(10000, 200000, 10000):
    #     x_axis.append(m)
    #     start1 = time.time()
    #     without_crt(x, p, m)
    #     end1 = time.time()
    #     t1.append(end1 - start1)
    #     start2 = time.time()
    #     crt(x, p, m)
    #     end2 = time.time()
    #     t2.append(end2 - start2)
    # plt.plot(x_axis, t1, color='r', label='without')
    # plt.plot(x_axis, t2, color='g', label='with')
    # plt.xlabel("m")
    # plt.ylabel("calculation time")
    # plt.title("comparison of calculation time <x^p mod m> without and with CRT \nwhen x = 12345; p = 67890; for m in range(10000, 200000, 10000)")
    # plt.legend()
    # plt.show()

    x = 12345
    m = 67890
    t1 = []
    t2 = []
    x_axis = []
    for p in range(10000, 200000, 10000):
        x_axis.append(p)
        start1 = time.time()
        without_crt(x, p, m)
        end1 = time.time()
        t1.append(end1 - start1)
        start2 = time.time()
        crt(x, p, m)
        end2 = time.time()
        t2.append(end2 - start2)
    plt.plot(x_axis, t1, color='r', label='without')
    plt.plot(x_axis, t2, color='g', label='with')
    plt.xlabel("p")
    plt.ylabel("calculation time")
    plt.title("comparison of calculation time <x^p mod m> without and with CRT \nwhen x = 12345; m = 67890; for p in range(10000, 200000, 10000)")
    plt.legend()
    plt.show()

    # m = 12345
    # p = 67890
    # t1 = []
    # t2 = []
    # x_axis = []
    # for x in range(10000, 200000, 10000):
    #     x_axis.append(x)
    #     start1 = time.time()
    #     without_crt(x, p, m)
    #     end1 = time.time()
    #     t1.append(end1 - start1)
    #     start2 = time.time()
    #     crt(x, p, m)
    #     end2 = time.time()
    #     t2.append(end2 - start2)
    # plt.plot(x_axis, t1, color='r', label='without')
    # plt.plot(x_axis, t2, color='g', label='with')
    # plt.xlabel("x")
    # plt.ylabel("calculation time")
    # plt.title(
    #     "comparison of calculation time <x^p mod m> without and with CRT \nwhen m = 12345; p = 67890; for x in range(10000, 200000, 10000)")
    # plt.legend()
    # plt.show()


