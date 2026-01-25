from sage.all import *

q = 131
Fq = GF(q)


R = PolynomialRing(Fq, 'i')
i = R.gen()
f = i**2 + 1

Rext = Fq.extension(f, 'i')
i = Rext.gen()

E_2 = EllipticCurve(Rext, [0, 5])
print(E_2)

P = E_2(2,12)
Q = E_2(67,56)

lam = (Q[1]-P[1])/(Q[0]-P[0])
nu = P[1] - lam*P[0]

x,y = Rext.gens()
l = Curve(Rext,[y-(lam*x+nu)])
print(l)
print(IntersectionPoints(E_2,l))




print(P)
print(Q)
print(P+Q)
