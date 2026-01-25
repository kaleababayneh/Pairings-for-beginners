from sage.all import *

q = random_prime(2**50, lbound=2**49)
print(q)

Fq = GF(q)

a = Fq.random_element()
b = Fq.random_element()
E = EllipticCurve(Fq, [a, b])

P = E.random_point()
Q = E.random_point()
R = E.random_point()
S = E.random_point()

print(E.divisor(P))
print(E.divisor(Q))
print(E.divisor(R))
print(E.divisor(S))


D1 = 2*E.divisor(P) - 3*E.divisor(Q)
D2 = 3*E.divisor(Q) + E.divisor(R) - E.divisor(S)


print(D1)
print(D2)
print(D1 + D2)

print(sum(c for c, p in D1))
print(sum(c for c, p in D2))
print(sum(c for c, p in D1 + D2))


