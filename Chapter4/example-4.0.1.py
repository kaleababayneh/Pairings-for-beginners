from sage.all import *

q = 7691
Fq = GF(q)


a = Fq(0)
b = Fq(1)

R = PolynomialRing(Fq, 'i')
i = R.gen()
f = i**2 + 1

E = EllipticCurve(Fq, [a, b])
Fq_2 = GF(q**2, name='i', modulus=f)
E_2 = EllipticCurve(Fq_2, [a, b])

print(E.order().factor())
print(E_2.order().factor())

P = E_2(2693, 4312)  
Q = E_2(633*i + 6145, 7372*i + 109)

r = 641

print(P.weil_pairing(Q, r))
print(P.weil_pairing(Q, r)**r)

a = 403
b = 135

print(a*P)
print(b*Q)

print((a * P).weil_pairing(Q, r))
print(P.weil_pairing(Q, r)**a)

print(P.weil_pairing(b * Q, r))
print(P.weil_pairing(Q, r)**b)

print((a * P).weil_pairing(b * Q, r))
print(P.weil_pairing(Q, r)**(a*b))