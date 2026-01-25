from sage.all import *
import random
q = 11
Fq = GF(q)

a = Fq(0)
b = Fq(4)

R = PolynomialRing(Fq, 'i')
i = R.gen()
f = i**2 + 1
Fq_2 = GF(q**2, name='i', modulus=f)

E = EllipticCurve(Fq, [a, b])
E_2 = EllipticCurve(Fq_2, [a, b])

print(list(E.order().factor()))
print(list(E_2.order().factor()))

r = 3
# print points in order 3 
torsion_r = E(0).division_points(r)
torsion_r_2 = E_2(0).division_points(r)

print(torsion_r)
print(torsion_r_2)

print(len(torsion_r))
print(len(torsion_r_2))


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
        V = set(j * P for j in range(1, pts_in_pet + 1))
        T.append(V)
    
    return T


print("\n--- Flower Generator ---")
petals = flower_generator(torsion_r_2)

for i, petal in enumerate(petals):
    print(f"Petal {i+1}: {(petal)}")
