from sage.all import *


RR = RealField()
R = PolynomialRing(RR, 'i')
i = R.gen()
f = i**2 + 1

Rext = RR.extension(f, 'i')
i = Rext.gen()

E_2 = EllipticCurve(Rext, [3, 0])
print(E_2)

E1 = E_2(12,24,4)
E2 = E_2(-3*i, -6*i, -1*i)
E3 = E_2(3*i, 6*i, i)
print(E1)
print(E2)
print(E3)
print(E1 == E2)
print(E2 == E3)
print(E1 == E3)