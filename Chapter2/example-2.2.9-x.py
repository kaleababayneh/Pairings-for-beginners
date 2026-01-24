from sage.all import *

p = 101
Fq = GF(p)

# Curve: y^2 = x^3 + x + 1 over F_101
E = EllipticCurve(Fq, [1, 1])
O = E(0)

print("E =", E)
print("#E(Fq) =", E.order(), "=", factor(E.order()))

# Division polynomials (x-only, for odd r; for r=2 Sage gives an x-polynomial related to 2-torsion)
psi2  = E.division_polynomial(2, two_torsion_multiplicity=2)
psi3  = E.division_polynomial(3)
psi5  = E.division_polynomial(5)
psi7  = E.division_polynomial(7)
psi11 = E.division_polynomial(11)

def roots_only(poly):
    """Return just the roots (no multiplicities), like Magma Roots(...) list of pairs."""
    return [r for (r, mult) in poly.roots()]

def points_with_x(E, x):
    """
    Sage analogue of Magma Points(E, x):
    all points (x,y) in E(Fq) with given x-coordinate.
    """
    F = E.base_field()
    x = F(x)
    rhs = x**3 + E.a4()*x + E.a6()  # for short Weierstrass y^2 = x^3 + a4*x + a6
    if rhs == 0:
        return [E(x, F(0))]
    if rhs.is_square():
        y = rhs.sqrt()
        if y == 0:
            return [E(x, F(0))]
        return [E(x, y), E(x, -y)]
    return []  # no points over this base field

# --- Roots(psi2), Roots(psi3), ... ---
print("\nRoots(psi2) =", psi2.roots())
print("Roots(psi3) =", psi3.roots())
print("Roots(psi5) =", psi5.roots())
print("Roots(psi7) =", psi7.roots())
print("Roots(psi11) =", psi11.roots())

# --- Mimic Magma's selection of x1, x2, x3 and Points(E, x) ---
# psi3
r3 = roots_only(psi3)
print("\npsi3 x-roots:", r3)
if len(r3) >= 2:
    x1, x2 = r3[0], r3[1]
    print("Points(E, x1) for x1 =", x1, ":", points_with_x(E, x1))
    print("Points(E, x2) for x2 =", x2, ":", points_with_x(E, x2))

# psi5
r5 = roots_only(psi5)
print("\npsi5 x-roots:", r5)
if len(r5) >= 2:
    x1, x2 = r5[0], r5[1]
    print("Points(E, x1) for x1 =", x1, ":", points_with_x(E, x1))
    print("Points(E, x2) for x2 =", x2, ":", points_with_x(E, x2))

# psi7
r7 = roots_only(psi7)
print("\npsi7 x-roots:", r7)
if len(r7) >= 3:
    x1, x2, x3 = r7[0], r7[1], r7[2]
    print("Points(E, x1) for x1 =", x1, ":", points_with_x(E, x1))
    print("Points(E, x2) for x2 =", x2, ":", points_with_x(E, x2))
    print("Points(E, x3) for x3 =", x3, ":", points_with_x(E, x3))
