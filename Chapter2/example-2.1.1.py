from sage.all import *


RR = RealField()

# Polynomial ring
R = PolynomialRing(RR, 'x')
x = R.gen()

f = x**3 - 2*x
y = x
# find the roots of f
roots = (y**2 - f).roots()
print(roots)
print("\n")

Rext = RR.extension(f, 'alpha')
alpha = Rext.gen()

E_2 = EllipticCurve(Rext, [-2, 0])
print(E_2)


P1 = E_2(-1, -1)
P2 = E_2(0, 0)
P3 = E_2(2, 2)

print(P1, "+", P2, "=", -P3, "=>", P1 + P2 == -P3)

y2 = -1/2*x - 3/2
print("\n")
print((y2**2 - f).roots())
print("\n")
print(2*P1)
