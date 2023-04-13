#1 Classes: Dealing with Complex Numbers

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex((self.real+no.real), self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex((self.real-no.real), (self.imaginary-no.imaginary))

    def __mul__(self, no):
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return Complex(r, i)

    def __truediv__(self, no):
        conjugate = Complex(no.real, (-no.imaginary))
        num = self*conjugate
        denom = no*conjugate
        try:
            return Complex((num.real/denom.real), (num.imaginary/denom.real))
        except Exception as e:
            print(e)

    def mod(self):
        m = math.sqrt(self.real**2+self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)

    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


#2 Class 2 - Find the Torsional Angle


import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return  Points((self.x-no.x), (self.y-no.y), (self.z-no.z))

    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)

    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y), (self.z*no.x-self.x*no.z), (self.x*no.y-self.y*no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    POINTS = list()
    for i in range(4):
        A = list(map(float, input().split()))
        POINTS.append(A)

    A, B, C, D = Points(*POINTS[0]), Points(*POINTS[1]), Points(*POINTS[2]), Points(*POINTS[3])
    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    ANGLE = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

    print("%.2f" % math.degrees(ANGLE))