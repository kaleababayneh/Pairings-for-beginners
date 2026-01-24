from sage.all import *

p = 13
Fp = GF(p)
E = EllipticCurve(Fp, [2, 1])


print(E.order())
print(E.order().factor())

psi3 = E.division_polynomial(3)
print(psi3)
psi5 = E.division_polynomial(5)
print(psi5)

print(psi3.roots())
print(psi5.roots())
