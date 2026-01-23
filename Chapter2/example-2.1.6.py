from sage.all import *


QQ = RationalField()
QR = PolynomialRing(QQ,'i')
i = QR.gen()
f = i**2 + 2

Qext = QQ.extension(f,'i')
i = Qext.gen()
E = EllipticCurve(QQ,[0,-2])
E_ext = E.base_extend(Qext)

def DBL(P):
    E = P.curve()
    O = E(0)
    if P == O:
        return O

    xP, yP = P.xy()
    if yP == 0:
        return O  # tangent is vertical

    lam = (3 * xP**2) / (2 * yP)   # a=0
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

P = E(3,5)
S = E_ext(0,i)

print(P)
print(S)

print("2*P == DBL(P) ?", (2*P == DBL(P)))

Qpt = DBL(P)
print("ADD(P, DBL(P)) == (P + DBL(P)) ?", (ADD(P, Qpt) == (P + Qpt)))

Rpt = P + Qpt
print("3*P == (P + DBL(P)) ?", (3*P == Rpt))


def int_to_sequence_base(n, base=2):
    
    n = Integer(n)
    return n.digits(base)  # least-significant digit first

for n in [10, 100, 1000]:
    y = (n*P).xy()[1]              # y-coordinate
    denom = y.denominator()
    print(f"digits base 2 (LSB first) =", len(int_to_sequence_base(denom, 2)))
    print()