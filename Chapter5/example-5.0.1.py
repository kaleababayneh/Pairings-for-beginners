from sage.all import *
import random

q = 23
Fq = GF(q)
a = Fq(17)
b = Fq(6)
E = EllipticCurve(Fq, [a, b])

r = 5

P = E(10,7)

O = E(0)

D1 = E.divisor(P) - E.divisor(O)
D2  =  2 * E.divisor(P) - E.divisor(2*P) - E.divisor(O)
D3 = 3 * E.divisor(P) - E.divisor(3*P) - 2 * E.divisor(O)
D4 = 4 * E.divisor(P) - E.divisor(4*P) - 3 * E.divisor(O)
D5 = 5 * E.divisor(P) - E.divisor(5*P) - 4 * E.divisor(O)

print(D1)
print(D2)
print(D3)
print(D4)
print(D5)


R = PolynomialRing(Fq, ['x', 'y'])
x, y = R.gens()



def fDBL(P):
    xP, yP = P.xy()
    lambda_ = (3*xP**2 + a)/(2*yP)
    c = yP - lambda_*xP
    l = y - (lambda_*x + c)
    v = x - (lambda_**2 - 2*xP)
    return l/v

def fADD(P, Q):
    xP, yP = P.xy()
    xQ, yQ = Q.xy()
    lambda_ = (yQ - yP)/(xQ - xP)
    c = yP - lambda_*xP
    l = y - (lambda_*x + c)
    v = x - (lambda_**2 - xP - xQ)
    return l/v

lPP = fDBL(P)
lP2P = fADD(P, 2*P)
lP3P = fADD(P, 3*P)
# fP4P = fADD(P, 4*P);  THIS IS DEFINED AS 1, since 4*P = -P and x - x_(-P) = x - x_P
lP4P = (x - 10)

f5P = lPP * lP2P * lP3P * lP4P
print("f5P =", f5P)
