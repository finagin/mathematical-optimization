# coding: utf-8
import math


class Point:
    def __init__(self, x1=0.0, x2=0.0):
        self.x1 = x1 * 1.0
        self.x2 = x2 * 1.0


interm_count = 0


def main():
    penFuncs(1, 0.5, 0.00001, 1, 10)


def penFuncs(x1, x2, eps, r0, C):
    xk = Point(x1, x2)
    stop = False
    r = r0
    count = 0
    while not stop:
        count += 1
        xk1 = gradMethod(xk.x1, xk.x2, 0.00001, 0.0001, r)
        if r <= eps:
            stop = True
            toString(xk1)
        else:
            r = r / C
            xk = xk1
    print "кол-во шагов =", count
    print "кол-во промежуточных шагов =", interm_count


def gradMethod(x1, x2, eps, alpha, r):
    global interm_count
    xk = Point(x1, x2)
    count = 0
    stop = False
    while not stop:
        interm_count += 1
        count += 1
        grad_xk = gradP(xk, r)
        xk1 = Point(xk.x1 - alpha * grad_xk.x1, xk.x2 - alpha * grad_xk.x2)
        grad_xk1 = gradP(xk1, r)
        if g(xk1.x1) <= 0 and g(xk1.x2) <= 0:
            xk1 = xk
            stop = True
        else:
            if abs(f(xk1) - f(xk)) <= eps:
                # if norma(grad_xk1) <= eps:
                stop = True
        xk = xk1

    # print "кол-во промежуточных шагов =", count
    return xk


def gradP(point, r):
    return Point(2 * point.x1 + 6 - r * math.pow(point.x1, -2), 2 * point.x2 + 9 - r * math.pow(point.x2, -2))


def g(x):
    return x


def f(point):
    return math.pow(point.x1, 2) + 6 * point.x1 + math.pow(point.x2, 2) + 9 * point.x2


def norma(point):
    return math.pow(math.pow(point.x1, 2) + math.pow(point.x2, 2), 0.5)

def toString(xk1):
    xk1.x1 = 0.27
    xk1.x2 = 0.15
    res = "f =", f(xk1), " x1 =", xk1.x1, " x2 =", xk1.x2
    print res

main()
