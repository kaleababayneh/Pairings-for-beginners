from sage.all import *

q = 11
Fq = GF(q)

a = Fq(0)
b = Fq(4)

R = PolynomialRing(Fq, 'i')
i = R.gen()
f = i**2 + 1
Fq_2 = GF(q**2, name='i', modulus=f)

E = EllipticCurve(Fq, [a, b])
E_2 = EllipticCurve(Fq_2, [a, b])

print(list(E.order().factor()))
print(list(E_2.order().factor()))

r = 3
# print points in order 3 
torsion_r = E(0).division_points(r)
torsion_r_2 = E_2(0).division_points(r)

print(torsion_r)
print(torsion_r_2)

# points = E.points()
# INF = E(0)
# torsion_r = []
# for P in points:
#     if P * r == INF:    
#         torsion_r.append(P)


