from sage.all import *

# --- curve / field setup ---
q = 23
Fq = GF(q)
a = Fq(-1)
b = Fq(0)
E = EllipticCurve(Fq, [a, b])

P = E(2, 11)
r = 3
k = 2

Rk = PolynomialRing(Fq, 'u')
u = Rk.gen()
Fqk = GF(q**k, name='u', modulus=u**k + 1)   # i^2 = -1
uk = Fqk.gen()
Ek = EllipticCurve(Fqk, [a, b])

# function field variables (formal x,y)
RR = PolynomialRing(Fqk, ['x', 'y'])
x, y = RR.gens()

def line_func(A, B):
    """
    Returns l_{A,B}(x,y), the line through A and B (or tangent if A=B),
    as a polynomial in (x,y) over Fqk.
    """
    if A.is_zero() or B.is_zero():
        return RR(1)

    xA, yA = map(Fqk, A.xy())
    xB, yB = map(Fqk, B.xy())

    # vertical line: B = -A  <=>  xA = xB and yA = -yB
    if xA == xB and yA == -yB:
        return x - xA

    # tangent case
    if A == B:
        lam = (3*xA**2 + Fqk(a)) / (2*yA)
    else:
        lam = (yB - yA) / (xB - xA)

    c = yA - lam*xA
    # line: y - (lam*x + c)
    return y - (lam*x + c)

def vert_func(T):
    """
    v_T(x) = x - x(T), except v_O = 1
    """
    if T.is_zero():
        return RR(1)
    xT = Fqk(T.xy()[0])
    return x - xT

def miller_f(r, P):
    """
    Computes Miller function f_{r,P} with divisor (f) = r(P) - (rP) - (r-1)(O).
    For rP = O (r-torsion), this matches the usual f_{r,P} up to an r-th power constant.
    """
    R = Ek(P)          # lift to Ek
    f = RR(1)
    bits = Integer(r).digits(2)
    # iterate from next-to-msb down to lsb
    for b in bits[-2::-1]:
        # doubling step
        l = line_func(R, R)
        v = vert_func(2*R)
        f = f**2 * (l / v)
        R = 2*R

        # addition step
        if b == 1:
            l = line_func(R, Ek(P))
            v = vert_func(R + Ek(P))
            f = f * (l / v)
            R = R + Ek(P)
    return f

frP = miller_f(r, P)
print("f_{r,P} =", frP)

# Optional: simplify / normalize a bit
print("Numerator:", frP.numerator())
print("Denominator:", frP.denominator())
