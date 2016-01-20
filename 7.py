# coding: utf-8
import math


class Point:
    def __init__(self, x1=0.0, x2=0.0):
        self.x1 = x1 * 1.0
        self.x2 = x2 * 1.0


a = 1.0
b = -1.4
c = 0.01
d = 0.11

interm_count = 0


def main():
    gradMethod(1.0, 0.0, 0.0001, 0.001)
    print
    print "============================="
    print
    downhillMethod(1.0, 0.0, 0.0001)

    # gradMethod(5.0, 5.0, 0.001, 0.001)
    # print
    # print "============================="
    # print
    # downhillMethod(5, 5, 0.001)


def gradFp(point):
    global a, b, c, d
    # return Point(a + math.exp(c * point.x1 + d * point.x2) * c, b + math.exp(c * point.x1 + d * point.x2) * d)
    return Point(18 * 2 * point.x1 + 12, 15 * 2 * point.x2 + 17)


def norma(point):
    return math.pow(math.pow(point.x1, 2) + math.pow(point.x2, 2), 0.5)


def f(point):
    global a, b, c, d
    # return a * point.x1 + b * point.x2 + math.exp(c * point.x1 + d * point.x2)
    return 18 * math.pow(point.x1, 2) + 12 * point.x1 + 15 * math.pow(point.x2, 2) + 17 * point.x2 + 10


def gold(xk, a, b, eps):
    global interm_count
    iters = 0
    lambd = 1.618
    x = [0.0] * 5
    y = [0.0] * 5
    while b - a > eps:
        x[0] = b - (b - a) / lambd
        x[1] = a + (b - a) / lambd
        y[0] = func(xk, x[0])
        y[1] = func(xk, x[1])
        if y[0] <= y[1]:
            b = x[1]
            x[1] = x[0]
            y[1] = y[0]
            x[0] = a + b - x[1]
            y[0] = func(xk, x[0])
        else:
            a = x[0]
            x[0] = x[1]
            y[0] = y[1]
            x[1] = a + b - x[0]
            y[1] = func(xk, x[1])
        iters += 1
        interm_count += 1
    # print "кол-во промежуточных шагов =", iters
    if y[0] <= y[1]:
        return x[0]
    else:
        return x[1]


def func(xk, alpha):
    return f(Point(xk.x1 - alpha * gradFp(xk).x1, xk.x2 - alpha * gradFp(xk).x2))


def gradMethod(x1, x2, eps, alpha):
    xk = Point(x1, x2)
    count = 0
    stop = False
    while not stop:
        count += 1
        grad_xk = gradFp(xk)
        xk1 = Point(xk.x1 - alpha * grad_xk.x1, xk.x2 - alpha * grad_xk.x2)
        grad_xk1 = gradFp(xk1)

        # if abs(f(xk1) - f(xk)) <= eps:
        if norma(grad_xk1) <= eps:
            stop = True
            print "f =", f(xk1), " x1 =", xk1.x1, " x2 =", xk1.x2
            print "кол-во шагов =", count
        else:
            xk = xk1


def downhillMethod(x1, x2, eps):
    xk = Point(x1, x2)
    count = 0
    stop = False
    while not stop:
        count += 1
        grad_xk = gradFp(xk)
        alpha_k = gold(xk, 0, 1, eps)
        xk1 = Point(xk.x1 - alpha_k * grad_xk.x1, xk.x2 - alpha_k * grad_xk.x2)

        grad_xk1 = gradFp(xk1)

        # if math.abs(f(xk1) - f(xk)) <= eps:
        if norma(grad_xk1) <= eps:
            stop = True
            print "f =", f(xk1), " x1 =", xk1.x1, " x2 =", xk1.x2
            print "кол-во шагов =", count
            print "кол-во промежуточных шагов =", interm_count
        else:
            xk = xk1


main()
