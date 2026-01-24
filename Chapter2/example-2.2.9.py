from sage.all import *

p = 101
Fp = GF(p)
E = EllipticCurve(Fp, [1, 1])

print(E.order().factor())
psi2 = E.division_polynomial(2)
psi3 = E.division_polynomial(3)
psi5 = E.division_polynomial(5)
psi7 = E.division_polynomial(7)
psi11 = E.division_polynomial(11)

print(E)
print(psi2.roots())
print(psi3.roots())
print(psi5.roots())
print(psi7.roots())
print(psi11.roots())




