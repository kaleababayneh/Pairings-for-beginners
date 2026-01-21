from sage.all import *

p = 11
Fp = GF(p)
E = EllipticCurve(Fp, [4, 3])

print(E)
print("Points on E:", E.points())
print("Order of E:", E.order())

R = PolynomialRing(Fp, 'i')
i = R.gen()
f = i**2 + 1
Fp_2 = GF(p**2, name='i', modulus=f)
E_2 = EllipticCurve(Fp_2, [4, 3])
print(E_2)
#print("Points on E_2:", E_2.points())
print("Order of E_2:", E_2.order())

P = E_2(2, 5*i)
Q = E_2(2*i+10, 7*i+2)
print(P)
print(Q)
print(P + Q)