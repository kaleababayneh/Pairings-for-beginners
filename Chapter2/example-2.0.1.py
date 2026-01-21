from sage.all import *

# Base field
QQ = RationalField()

# Polynomial ring
R = PolynomialRing(QQ, 'x')
x = R.gen()

# Quadratic extension QQ(alpha) with alpha^2 + 2 = 0
f = x**2 + 2
Qext = QQ.extension(f, 'alpha')   # creates the field
alpha = Qext.gen()               # the generator "alpha"

# Elliptic curve: y^2 = x^3 - 2  (Sage uses [a,b])
E = EllipticCurve(QQ, [0,-2])

# Base change to Qext
Eext = E.base_extend(Qext)

# Points
P = E(3, 5)
S = Eext(0, alpha)
print("P  =", P)
print("2P =", 2*P)
print("P+2P =", P+2*P)
print("3P =", 3*P)
print("S  =", S)
