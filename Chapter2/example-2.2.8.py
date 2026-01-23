from sage.all import *

q = 67
Fq = GF(q)

E = EllipticCurve(Fq, [4, 3])
O = E(0)

t = E.trace_of_frobenius()

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

def frob_poly_identity_holds(EK, P, q, t):
    """Check π^2(P) - t*π(P) + q*P == O."""
    O = EK(0)
    piP  = pi_q_on_E(EK, P, q)
    pi2P = pi_q_on_E(EK, piP, q)
    return (pi2P - t*piP + q*P) == O, (pi2P - t*piP + q*P)


# -----------------------
# P in E(Fq)
# -----------------------
P = E(15, 50)
print("\nP =", P)

piP = pi_q_on_E(E, P, q)
print("pi(P) =", piP)
print("pi(P) == P ?", piP == P)

ok, expr = frob_poly_identity_holds(E, P, q, t)
print("pi^2(P) - t*pi(P) + q*P == O ?", ok)
print("Value:", expr)

# -----------------------
# P2 in E(Fq2)
# -----------------------
P2 = E2(2*u + 16, 30*u + 39)
print("\nP2 =", P2)

piP2 = pi_q_on_E(E2, P2, q)
pi2P2 = pi_q_on_E(E2, piP2, q)
print("pi^2(P2) == P2 ?", pi2P2 == P2)

ok2, expr2 = frob_poly_identity_holds(E2, P2, q, t)
print("pi^2(P2) - t*pi(P2) + q*P2 == O2 ?", ok2)
print("Value:", expr2)

# -----------------------
# P3 in E(Fq3)
# -----------------------
P3 = E3(19*v**2 + 49*v + 8, 20*v**2 + 66*v + 21)
print("\nP3 =", P3)

ok3, expr3 = frob_poly_identity_holds(E3, P3, q, t)
print("pi^2(P3) - t*pi(P3) + q*P3 == O3 ?", ok3)
print("Value:", expr3)
