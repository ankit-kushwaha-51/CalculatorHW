from CsvReader import CsvReader
import math as math


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a*b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = round(b/a, 9)
    return c


def square(a):
    a = int(a)
    b = a*a
    return b


def squareroot(a):
    a = float(a)
    b = round(a**(1.0/2), 8)
    return b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result