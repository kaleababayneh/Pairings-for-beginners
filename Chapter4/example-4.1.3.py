from sage.all import *

q = 11
Fq = GF(q)

a = Fq(7)
b = Fq(2)


R = PolynomialRing(Fq, 'i')
i = R.gen()
f = R.irreducible_element(3)
Fq_3 = GF(q**3, name='i', modulus=f)

E = EllipticCurve(Fq, [a, b])
E_3 = EllipticCurve(Fq_3, [a, b])

print(list(E.order().factor()))
print(list(E_3.order().factor()))
r = 7
torsion_r = E(0).division_points(r)
torsion_r_3 = E_3(0).division_points(r)
print(torsion_r)
print(torsion_r_3)
print(len(torsion_r))
print(len(torsion_r_3))
