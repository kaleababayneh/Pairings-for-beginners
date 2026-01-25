from sage.all import *
import random


q = 59
Fq = GF(q)

a = Fq(0)
b = Fq(1)

E = EllipticCurve(Fq, [a, b])
r = 5
k = 2

R = PolynomialRing(Fq, 'u')
u = R.gen()
f = u**2 + 1

Fq_2 = GF(q**2, name='u', modulus=f)
u = Fq_2.gen()
E_2 = EllipticCurve(Fq_2, [a, b])

torsion_pts = E_2(0).division_points(r)

zeta3 = Fq_2(24)*u + Fq_2(29)
g1_torsion_pts = E(0).division_points(r)


def phi(P):
    if P.is_zero():
        return P
    xP, yP = P.xy()
    return E_2(zeta3 * xP, yP)


def flower_generator(tors_pts):

    V = set()
    S = set(tors_pts)
    petals = int(len(S)**0.5) + 1  # sqrt(#S) + 1
    pts_in_pet = petals - 1
    T = []
    
    for i in range(petals):
        S = S - V
        if not S:
            break
        candidates = [P for P in S if not P.is_zero()]
        if not candidates:
            break
        P = random.choice(candidates)
        # Generate the petal: {1*P, 2*P, ..., (petals-1)*P}
        V = set(P * j for j in range(1, pts_in_pet + 1))
        T.append(V)
    
    return T


# mulitply the x coordinate of g1_torsion_pts by zeta3
ph1 = [phi(P) for P in g1_torsion_pts]
ph2 = [phi(P) for P in ph1]
ph3 = [phi(P) for P in ph2]
ph4 = [phi(P) for P in ph3]
ph5 = [phi(P) for P in ph4]
ph6 = [phi(P) for P in ph5]


print("\n--- Flower Generator ---")
petals = flower_generator(torsion_pts)
for petal in petals:
    print(petal)


print("\n--- phi ---")
print(ph1)
print(ph2)
print(ph3)
print(ph4)
print(ph5)
print(ph6)
