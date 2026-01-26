from sage.all import *
import random

q = 23
Fq = GF(q)
a = Fq(-1)
b = Fq(0)
E = EllipticCurve(Fq, [a, b])


P = E(2,11)


r = 3
k = 2

R = PolynomialRing(Fq, 'u')
u = R.gen()
f = u**k + 1

Fq_k = GF(q**k, name='u', modulus=f)
u = Fq_k.gen()
E_k = EllipticCurve(Fq_k, [a, b])

print(E_k)

torsion_r = E(0).division_points(r)
torsion_r_2 = E_k(0).division_points(r)

print(torsion_r)
print(torsion_r_2)

# O = E(0)

R = PolynomialRing(Fq, ['x', 'y'])
x, y = R.gens()


def fDBL(P):
    xP, yP = P.xy()
    lambda_ = (3*xP**2 + a)/(2*yP)
    c = yP - lambda_*xP
    l = y - (lambda_*x + c)
    v = x - (lambda_**2 - 2*xP)
    return l/v

def fADD(P, Q):
    xP, yP = P.xy()
    xQ, yQ = Q.xy()
    lambda_ = (yQ - yP)/(xQ - xP)
    c = yP - lambda_*xP
    l = y - (lambda_*x + c)
    v = x - (lambda_**2 - xP - xQ)
    return l/v

print(fDBL(P))

