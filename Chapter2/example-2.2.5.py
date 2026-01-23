from sage.all import *

q = 67
Fq = GF(q)

E = EllipticCurve(Fq, [4, 3])
O = E(0)

R1 = PolynomialRing(Fq, 'u')
u = R1.gen()
f = u**2 + 1
Fp_2 = GF(q**2, name='u', modulus=f)
E2 = EllipticCurve(Fp_2, [4, 3])
O2 = E2(0)

R2 = PolynomialRing(Fq, 'v')
v = R2.gen()
f2 = v**3 + 2
Fp_3 = GF(q**3, name='v', modulus=f2)
E3 = EllipticCurve(Fp_3, [4, 3])
O3 = E3(0)

def pi_q_on_E(EK, P, q):
    O = EK(0)
    if P == O:
        return O
    X, Y = P.xy()
    return EK(X**q, Y**q)

P = E(15,50)
print("P1 =", P)
print("pi_q(P1) =", pi_q_on_E(E, P, q))
print(E.order())
P2 = E2(2*u + 16, 30*u + 39)
print("P2 =", P2)
print("pi_q(P2) =", pi_q_on_E(E2, P2, q))
P3 = E3(15*v**2 + 4*v + 8, 44*v**2 + 30*v + 21)
print("P3 =", P3)
print("pi_q(P3) =", pi_q_on_E(E3, P3, q))
print("pi_q^2(P3) =", pi_q_on_E(E3, pi_q_on_E(E3, P3, q), q))