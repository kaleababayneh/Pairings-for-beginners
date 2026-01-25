from sage.all import *

# ----- Choose a small prime p (<= 2^29) but make the field size ~ 2^50 via p^2
p = random_prime(2**25, lbound=2**24)      # ~25-bit prime
Fq = GF(p**2, name='u')                   # |Fq| ≈ 2^50, characteristic p

# Random curve coefficients
a = Fq.random_element()
b = Fq.random_element()

# Elliptic curve for random points
E = EllipticCurve(Fq, [a, b])             # y^2 = x^3 + a*x + b

# Build the *projective plane curve* model and its function field
P2 = ProjectiveSpace(Fq, 2, names=('X','Y','Z'))
X, Y, Z = P2.gens()
C = Curve(Y**2*Z - X**3 - a*X*Z**2 - b*Z**3, P2)

K = C.function_field()
x, y = K.gens()                           # function field generators

def DBL(P):
    # Tangent line at P as a function: y - (lambda*x + nu)
    O = E(0)
    if P == O:
        return K(1)

    xP, yP = P.xy()
    if yP == 0:
        return x - xP                     # vertical tangent

    lam = (3*xP**2 + a) / (2*yP)
    nu  = yP - lam*xP
    return y - (lam*x + nu)

def ADD(P, Q):
    # Secant line through P,Q as a function: y - (lambda*x + nu)
    O = E(0)
    if P == O or Q == O:
        return K(1)
    if P == Q:
        return DBL(P)

    xP, yP = P.xy()
    xQ, yQ = Q.xy()
    if xP == xQ:
        return x - xP                     # vertical line (incl. Q = -P)

    lam = (yQ - yP) / (xQ - xP)
    nu  = yP - lam*xP
    return y - (lam*x + nu)

# Random points
P = E.random_point()
Q = E.random_point()
R = E.random_point()

# Magma: l:=ADD(P,Q); Support(Divisor(l));
l = ADD(P, Q)
print("Support(Divisor(l))  =", l.divisor().support())

# Magma: ld:=DBL(R); Support(Divisor(ld));
ld = DBL(R)
print("Support(Divisor(ld)) =", ld.divisor().support())

# Magma: lquot:=l/ld; Support(Divisor(lquot));
lquot = l / ld
print("Support(Divisor(l/ld)) =", lquot.divisor().support())
