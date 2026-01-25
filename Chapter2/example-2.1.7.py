from sage.all import *

p = 23
Fq = GF(p)
a = Fq(5)
b = Fq(7)

E = EllipticCurve(Fq, [a, b])
O = E(0)  # point at infinity


P = E(2, 5)
Q = E(12, 1)

print("P =", P)
print("Q =", Q)

def DBL(P):
    E = P.curve()
    O = E(0)
    if P == O:
        return O

    xP, yP = P.xy()
    if yP == 0:
        return O  # tangent is vertical

    a = E.a4()
    lam = (3 * xP**2 + a) / (2 * yP)   # a=0
    nu = yP - lam * xP
    X = lam**2 - 2 * xP
    Y = -(lam * X + nu)
    return E(X, Y)

def ADD(P, Q):

    if P == O:
        return Q
    if Q == O:
        return P
    if P == Q:
        return DBL(P)

    xP, yP = P.xy()
    xQ, yQ = Q.xy()

    # vertical line: P + (-P) = O
    if xP == xQ:
        return O

    lam = (yQ - yP) / (xQ - xP)
    nu = yP - lam*xP
    X = lam**2 - xP - xQ
    Y = -(lam*X + nu)

    print("lambda =", lam, "nu =", nu)
    return E(X, Y)


print("ADD(P,Q) == P+Q ?", ADD(P, Q) == (P + Q))

R = P + Q
print("R = P+Q =", R)

print("DBL(P) == 2*P ?", DBL(P) == (2*P))

S = 2*P
print("S = 2*P =", S)
