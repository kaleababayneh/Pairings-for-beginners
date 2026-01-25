from sage.all import *
from library import *


q = random_prime(2**50, lbound=2**49)
print(q)

Fq = GF(q)

a = Fq.random_element()
b = Fq.random_element()
E = EllipticCurve(Fq, [a, b])

P = E.random_point()
Q = E.random_point()
R = E.random_point()

l = ADD(P,Q)
print(l)

ld = DBL(R)

lquot = l/ld
print(lquot)