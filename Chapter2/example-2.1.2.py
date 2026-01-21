from sage.all import *

p = 11
Fp = GF(p)
E = EllipticCurve(Fp, [-2, 0])
R = PolynomialRing(Fp, 'x')
x = R.gen()
f = x**3 - 2*x
y = x
print((y**2 - f).roots())
print(E)
print("Points on E:", E.points())
print("Order of E:", E.order())

P = E(5,7)
Q = E(8,10)
print(P+Q)

y2 = x + 2
print((y2**2 - f).roots())