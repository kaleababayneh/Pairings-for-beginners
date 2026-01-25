from sage.all import *

q = 31
Fq = GF(q)

a = Fq(0)
b = Fq(13)

E = EllipticCurve(Fq, [a, b])
r = 5
print(list(E.order().factor()))
torsion_r = E(0).division_points(r)
print(torsion_r)
print(len(torsion_r))