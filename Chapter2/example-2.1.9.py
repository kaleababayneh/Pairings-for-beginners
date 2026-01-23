from sage.all import *

def PROJADD(XP, YP, ZP, XQ, YQ, ZQ):

    A  = XP*ZQ - XQ*ZP
    B  = YP*ZQ - YQ*ZP
    ZPZQ = ZP*ZQ

    XR = A * ( ZPZQ * (B**2) - (A**2) * (XP*ZQ + XQ*ZP) )
    YR = ZPZQ * (XQ*YP - XP*YQ) * (A**2) - B * ( (B**2)*ZPZQ - (XP*ZQ + XQ*ZP)*(A**2) )
    ZR = ZPZQ * (A**3)

    return XR, YR, ZR


q = next_prime(ZZ.random_element(2**10))   # prime <= 1024-ish (like Magma's NextPrime(Random(0,2^10)))
Fq = GF(q)

while True:
    a = Fq.random_element()
    b = Fq.random_element()
    # discriminant for y^2 = x^3 + a*x + b over char != 2,3:
    if 4*a**3 + 27*b**2 != 0:
        break

E = EllipticCurve(Fq, [a, b])

P = E.random_point()
Q = E.random_point()

# Ensure projective reps (usually z=1 for finite points)
# Sage elliptic curve points support indexing [0],[1],[2] for (X,Y,Z).
XP, YP, ZP = P[0], P[1], P[2]
XQ, YQ, ZQ = Q[0], Q[1], Q[2]

XR, YR, ZR = PROJADD(XP, YP, ZP, XQ, YQ, ZQ)

# Construct the resulting point on E from projective coordinates
R = E([XR, YR, ZR])

print("q =", q)
print("E =", E)
print("P =", P)
print("Q =", Q)
print("R (from PROJADD) =", R)
print("Check R == P + Q ?", R == (P + Q))
