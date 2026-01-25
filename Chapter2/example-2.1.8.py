from sage.all import *

q = 1021
Fq = GF(q)

a = Fq(-3)
b = Fq(-3)

E = EllipticCurve(Fq, [a, b])
P = E(379, 1011)
O = E(0) 

m = 655


B = Integer(m).digits(2)
B_msb = list(reversed(B))

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

def ADD(Pt, Qt):
    if Pt == O:
        return Qt
    if Qt == O:
        return Pt
    if Pt == Qt:
        return DBL(Pt)

    xP, yP = Pt.xy()
    xQ, yQ = Qt.xy()

    if xP == xQ:
        return O 

    lam = (yQ - yP) / (xQ - xP)
    nu = yP - lam * xP
    X = lam**2 - xP - xQ
    Y = -(lam * X + nu)
    return E(X, Y)

def Scalar(m, P):

    B = Integer(m).digits(2)         # LSB-first
    B_msb = list(reversed(B))        # MSB-first

    R = P
    for bit in B_msb[1:]:
        R = DBL(R)
        if bit == 1:
            R = ADD(R, P)
    return R

print("Scalar(m,P) == m*P ?", Scalar(m, P) == m * P)
print("m*P =", m * P)
print("Scalar(m,P) =", Scalar(m, P))
