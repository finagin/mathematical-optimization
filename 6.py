# coding: utf-8
import math


def main():
    print("----Деление пополам----")
    mid(-2.0, 0.0, math.pow(10, -3))
    print
    print("----Золотое сечение----")
    gold(-2.0, 0.0, math.pow(10, -3))
    print
    print("-------Фибоначчи-------")
    fibb(-2.0, 0.0, 22)
    print


def func(x):
    return math.pow(x, 2) + 8 * math.exp(0.55 * x)


fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


def mid(a, b, eps):
    iters = 0
    minY = func(a)
    minI = 0
    x = [0.0] * 5
    x[2] = (a + b) / 2
    temp = 0
    while b - a > 2 * eps:
        x[0] = a
        x[1] = (a + x[2]) / 2
        x[3] = (x[2] + b) / 2
        x[4] = b

        for i in range(1, 3):
            if func(x[i]) <= minY:
                minY = func(x[i])
                minI = i

        a = x[minI - 1]
        b = x[minI + 1]
        x[2] = x[minI]
        iters += 1

    print "minY =", minY
    print "minX =", x[minI]
    print "iterations =", iters


def gold(a, b, eps):
    iters = 0
    lambd = 1.618
    x = [0.0] * 2
    y = [0.0] * 2

    while b - a > eps:
        x[0] = b - (b - a) / lambd
        x[1] = a + (b - a) / lambd
        y[0] = func(x[0])
        y[1] = func(x[1])
        if y[0] <= y[1]:
            b = x[1]
            x[1] = x[0]
            y[1] = y[0]
            x[0] = a + b - x[1]
            y[0] = func(x[0])
        else:
            a = x[0]
            x[0] = x[1]
            y[0] = y[1]
            x[1] = a + b - x[0]
            y[1] = func(x[1])

        iters += 1

    if y[0] <= y[1]:
        print "minY =", y[0]
        print "minX =", x[0]
        print "iterations =", iters
        return y[0]
    else:
        print "minY =", y[1]
        print "minX =", x[1]
        print "iterations =", iters
        return y[1]


def fibb(a, b, N):
    pass
    F = [0] * N
    for i in range(1, N+1):
        F[i - 1] = fib(i)

    x = [0.0] * 2
    y = [0.0] * 2

    for i in range(0, N - 1):
        x[0] = a + (b - a) * F[N - 3] / F[N - 1]
        x[1] = a + (b - a) * F[N - 2] / F[N - 1]
        y[0] = func(x[0])
        y[1] = func(x[1])

        if y[0] <= y[1]:
            b = x[1]
            x[1] = x[0]
            y[1] = y[0]
            x[0] = a + b - x[1]
            y[0] = func(x[0])
        else:
            a = x[0]
            x[0] = x[1]
            y[0] = y[1]
            x[1] = a + b - x[0]
            y[1] = func(x[1])

    if y[0] < y[1]:
        print "minY =", y[0]
        print "minX =", x[0]
        print "iterations =", N
        return y[0]
    else:
        print "minY =", y[1]
        print "minX =", x[1]
        print "iterations =", N
        return y[1]


main()
