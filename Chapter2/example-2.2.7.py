from sage.all import *

p = 17
Fp = GF(p)
a = Fp(10)
b = Fp(0)

E = EllipticCurve(Fp, [a, b])
O = E(0)
roots = [x for x in Fp if x**2 == -1]
print("Roots of x^2 = -1 in F_17:", roots)

i = roots[0]

P = E.random_point()
while P == O:
    P = E.random_point()

print("Random non-infinity P =", P)
xP, yP = P.xy()
Q = E(-xP, i*yP)
print("Image point Q = (-x, i*y) =", Q)


p = 19
Fp = GF(p)
a = Fp(10)
b = Fp(0)

R1 = PolynomialRing(Fp, 'u')
u = R1.gen()
f = u**2 + 1
print("Irreducible element of degree 2:", f)
Fp_2 = GF(p**2, name='u', modulus=f)
E2 = EllipticCurve(Fp_2, [a, b])



print("Image point Q = (-x, i*y) =", Q)

roots = [x for x in Fp_2 if x**2 == -1]
i = roots[1]
print("Roots of x^2 = -1 in F_17^2:", roots)    
P = E2(12, 10)
print("Random non-infinity P =", P)
xP, yP = P.xy()
Q = E2(-xP, i * yP)
print("Image point Q = (-x, i*y) =", Q)