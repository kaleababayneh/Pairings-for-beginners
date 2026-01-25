from sage.all import *

q = random_prime(2**50, lbound=2**49)
print(q)

Fq = GF(q)

a = Fq.random_element()
b = Fq.random_element()
E = EllipticCurve(Fq, [a, b])


def DBL(P):
    E = P.curve()
    print(E)
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
    E = P.curve()
    O = E(0)

    if P == O:
        return Q
    if Q == O:
        return P
    if P == Q:
        return DBL(P)

    xP, yP = P.xy()
    xQ, yQ = Q.xy()

    if xP == xQ:
        return O  # vertical line case (includes Q = -P)

    lam = (yQ - yP) / (xQ - xP)
    nu = yP - lam * xP
    X = lam**2 - xP - xQ
    Y = -(lam * X + nu)
    return E(X, Y)


P = E.random_point()
Q = E.random_point()


l = DBL(P)
print(l)


DP = E.divisor(P)
DQ = E.divisor(Q)


print(sum(c for c, p in DP))
print(sum(c for c, p in DQ))
