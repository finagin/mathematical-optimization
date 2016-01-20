# coding: utf-8
import math


class Point:
    def __init__(self, x1=0.0, x2=0.0):
        self.x1 = x1 * 1.0
        self.x2 = x2 * 1.0


iters = 0


def main():
    barrFuncs(0, 1, 0.001, 10, 10)
    # print B(Point(0.94389, 0.89635)) * 0.0001


def barrFuncs(x1, x2, eps, m0, bi):
    global iters
    xk = Point(x1, x2)
    stop = False
    m = m0
    while not stop:
        iters += 1
        xk1 = gradMethod(xk.x1, xk.x2, 0.00001, 0.001, m)
        # print "m =", m, " x1 =", xk1.x1, " x2 =", xk1.x2, " f =", f(xk1), " Q =", Q(xk1, m), " mB =", m * B(xk1)
        if m * B(xk1) <= eps:
            stop = True
            print "f =", f(xk1), " x1 =", xk1.x1, " x2 =", xk1.x2
        else:
            m = m / bi
            xk = xk1
    print "iters =", iters


def gradMethod(x1, x2, eps, alpha, m):
    global iters
    xk = Point(x1, x2)
    count = 0
    stop = False
    while not stop:
        iters += 1
        grad_xk = gradP(xk, m)
        xk1 = Point(xk.x1 - alpha * grad_xk.x1, xk.x2 - alpha * grad_xk.x2)
        grad_xk1 = gradP(xk1, m)
        if g(xk1) <= 0:
            xk1 = xk
            stop = True
        else:
            if norma(grad_xk1) <= eps:
                # if abs(f(xk1) - f(xk)) <= eps:
                stop = True
        xk = xk1
    return xk


def gradP(point, m):
    return Point(
        2 * point.x1 + 2 * point.x1 * m / math.pow(math.pow(point.x1, 2) - point.x2, 2) - 4 * point.x2 + 4 * math.pow(
            point.x1 - 2, 3), -4 * point.x1 + 8 * point.x2 - m / math.pow(math.pow(point.x1, 2) - point.x2, 2))


def g(point):
    return -1 * (math.pow(point.x1, 2) - point.x2)


def norma(point):
    return math.pow(math.pow(point.x1, 2) + math.pow(point.x2, 2), 0.5)


def f(point):
    return math.pow(point.x1 - 2, 4) + math.pow(point.x1 - 2 * point.x2, 2)


def Q(point, m):
    return f(point) + m * B(point)


def B(point):
    return 1 / g(point)

main()
