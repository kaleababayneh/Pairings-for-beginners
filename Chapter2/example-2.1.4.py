from sage.all import *

p = 13
Fp = GF(p)
E = EllipticCurve(Fp, [0, 5])

print(E)
print("Points on E:", E.points())
print("Order of E:", E.order())


# R = PolynomialRing(Fp, 'i')
# i = R.gen()
# f = R.irreducible_element(2)
# Fp_2 = GF(p**2, name='i', modulus=f)
# E_2 = EllipticCurve(Fp_2, [0, 5])
# print(E_2)

# print("Points on E_2:", E_2.points())
# print("Order of E_2:", E_2.order())
