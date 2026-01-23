from sage.all import *

q = 19
Fq = GF(q)

E = EllipticCurve(Fq, [0, 5])
P = E(-1, 2)

roots_Fq = [z for z in Fq if z**3 == 1]
print("Cube roots of unity in F_19:", roots_Fq)

zeta3_Fq = next((z for z in roots_Fq if z != 1), None)
print("Chosen zeta3 in F_19:", zeta3_Fq)


if zeta3_Fq is not None:
    P_image = E(zeta3_Fq * P.xy()[0], P.xy()[1])
    print("E![P[1]*zeta3, P[2]] =", P_image)
else:
    print("No nontrivial cube root of unity exists in F_19 (so the map is trivial over F_19).")


q = 23
R1 = PolynomialRing(Fq, 'u')
u = R1.gen()
f = u**2 + 1
Fp_2 = GF(q**2, name='u', modulus=f)
E2 = EllipticCurve(Fp_2, [0, 5])
P2 = E2(-1, 2)

roots_Fp_2 = [z for z in Fp_2 if z**3 == 1]
print("Cube roots of unity in F_19^2:", roots_Fp_2)

zeta3_Fp_2 = next((z for z in roots_Fp_2 if z != 1), None)
print("Chosen zeta3 in F_19^2:", zeta3_Fp_2)


if zeta3_Fp_2 is not None:
    P2_image = E2(zeta3_Fp_2 * P2.xy()[0], P2.xy()[1])
    print("E2![P2[1]*zeta3, P2[2]] =", P2_image)
else:
    print("No nontrivial cube root of unity exists in F_19^2 (so the map is trivial over F_19^2).")



def endomorphism(E, P, x_transform, y_transform):

    x, y = P.xy()
    return E(x_transform * x, y_transform * y)

