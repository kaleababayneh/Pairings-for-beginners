from sage.all import *

# ============================================
# Part 1: Division polynomial quotient ring
# ============================================
q = 13
Fq = GF(q)

a = Fq(2)
b = Fq(1)
E = EllipticCurve(Fq, [a, b])

Poly = PolynomialRing(Fq, names=('x','y'))
x, y = Poly.gens()

Exy = y**2 - (x**3 + a*x + b)

l = 3
psi3_uni = E.division_polynomial(l)
psi3 = psi3_uni(x)

I3 = Poly.ideal([Exy, psi3])
R3 = Poly.quotient(I3, names=('xbar','ybar'))
xbar, ybar = R3.gens()

print("R3(x^(q^2)) =", R3(x**(q**2)))
print("R3(x)       =", R3(x))
print("xbar        =", xbar)

# ============================================
# Part 2: Line functions for pairings
# ============================================
print("\n" + "="*50)
print("Line Functions for Pairings")
print("="*50 + "\n")

q = random_prime(2**50, lbound=2**49)
print("q =", q)
Fq = GF(q)

a = Fq.random_element()
b = Fq.random_element()
# Ensure non-singular curve
while 4*a**3 + 27*b**2 == 0:
    a = Fq.random_element()
    b = Fq.random_element()

E = EllipticCurve(Fq, [a, b])
O = E(0)
print("E:", E)


def tangent_line_at(P):
    """
    Return the tangent line function at P as a lambda.
    Line: y - lambda*x - nu = 0
    Returns a function that evaluates this line at any point R.
    """
    if P == O:
        return lambda R: Fq(1)
    
    xP, yP = P.xy()
    a4 = E.a4()
    
    if yP == 0:
        # Vertical tangent: x - xP
        return lambda R: Fq(1) if R == O else R.xy()[0] - xP
    
    lam = (3*xP**2 + a4) / (2*yP)
    nu = yP - lam*xP
    
    def eval_line(R):
        if R == O:
            return Fq(1)
        xR, yR = R.xy()
        return yR - lam*xR - nu
    
    return eval_line


def secant_line_through(P, Q):
    """
    Return the secant line function through P and Q as a lambda.
    Handles P == Q (tangent), P == -Q (vertical), and P or Q at infinity.
    """
    if P == O:
        return tangent_line_at(Q)
    if Q == O:
        return tangent_line_at(P)
    if P == Q:
        return tangent_line_at(P)
    
    xP, yP = P.xy()
    xQ, yQ = Q.xy()
    
    if xP == xQ:
        # Vertical line: x - xP
        return lambda R: Fq(1) if R == O else R.xy()[0] - xP
    
    lam = (yQ - yP) / (xQ - xP)
    nu = yP - lam*xP
    
    def eval_line(R):
        if R == O:
            return Fq(1)
        xR, yR = R.xy()
        return yR - lam*xR - nu
    
    return eval_line


def vertical_line_at(P):
    """
    Return the vertical line function x - xP.
    """
    if P == O:
        return lambda R: Fq(1)
    
    xP = P.xy()[0]
    return lambda R: Fq(1) if R == O else R.xy()[0] - xP


# --- Test the line functions ---
P = E.random_point()
while P == O:
    P = E.random_point()

Q = E.random_point()
while Q == O or Q == P or Q == -P:
    Q = E.random_point()

R = E.random_point()
while R == O:
    R = E.random_point()

print("\nP =", P)
print("Q =", Q)
print("R =", R)

# Tangent line at P
l_tangent = tangent_line_at(P)
print("\n--- Tangent line at P ---")
print("l(P) =", l_tangent(P), "  (should pass through P, so ~0)")
print("l(-2P) =", l_tangent(-2*P), "  (tangent touches 2P, so passes through -2P)")
print("l(R) =", l_tangent(R), "  (random evaluation)")

# Secant line through P and Q
l_secant = secant_line_through(P, Q)
print("\n--- Secant line through P and Q ---")
print("l(P) =", l_secant(P), "  (should be ~0)")
print("l(Q) =", l_secant(Q), "  (should be ~0)")
print("l(-(P+Q)) =", l_secant(-(P+Q)), "  (should be ~0, line also passes here)")
print("l(R) =", l_secant(R), "  (random evaluation)")

# Vertical line at P
l_vert = vertical_line_at(P)
print("\n--- Vertical line at P ---")
print("v(P) =", l_vert(P), "  (should be 0)")
print("v(-P) =", l_vert(-P), "  (should be 0)")
print("v(R) =", l_vert(R), "  (random evaluation)")

print("\n--- Point arithmetic check ---")
print("2*P =", 2*P)
print("-2*P =", -2*P)
print("P + Q =", P + Q)
print("-(P+Q) =", -(P+Q))
