from sage.all import *
import random

q = 5
Fq = GF(q)
a = Fq(0)
b = Fq(-3)
E = EllipticCurve(Fq, [a, b])

k = 2
r = 3
R = PolynomialRing(Fq, 'u')
u = R.gen()
f = u**k + 2
Fq_k = GF(q**k, name='u', modulus=f)
u = Fq_k.gen()
Ek = EllipticCurve(Fq_k, [a, b])

order = E.order()
order_2 = Ek.order()
cofactor = order_2 // (r * r)
print(E.order())
print(Ek.order())
print(cofactor)


torsion_r = E(0).division_points(r)
torsion_r_2 = Ek(0).division_points(r)

print(torsion_r)
print(torsion_r_2)





def flower_generator(tors_pts):

    V = set()
    S = set(tors_pts)
    petals = int(len(S)**0.5) + 1  # sqrt(#S) + 1
    pts_in_pet = petals - 1
    T = []
    
    for _ in range(petals):
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


petals = flower_generator(torsion_r_2)


print("\n--- Flower Generator 1 ---")
for idx, petal in enumerate(petals):
    print(f"Petal {idx+1}: {(petal)}")

