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
i = Fq_2.gen()
E = EllipticCurve(Fq, [a, b])
E2 = EllipticCurve(Fq, [a, -b])
E_2 = EllipticCurve(Fq_2, [a, b])
E2_2 = EllipticCurve(Fq_2, [a, -b])


r = 3
# print points in order 3 
torsion_r = E(0).division_points(r)
torsion_r_2 = E_2(0).division_points(r)

torsion_r2 = E2(0).division_points(r)
torsion_r2_2 = E2_2(0).division_points(r)



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
petals2 = flower_generator(torsion_r2_2)

print("\n--- Flower Generator 1 ---")
for idx, petal in enumerate(petals):
    print(f"Petal {idx+1}: {(petal)}")

print("\n--- Flower Generator 2 ---")
for idx, petal in enumerate(petals2):
    print(f"Petal {idx+1}: {(petal)}")

######################
# Distortion maps between E: y^2 = x^3 + b and E': y^2 = x^3 - b
# These are isomorphisms over Fq_2 (where i exists with i^2 = -1)
#
# ψ: E'(Fq_2) → E(Fq_2)       is  (x, y) → (-x, i*y)
# ψ⁻¹: E(Fq_2) → E'(Fq_2)     is  (x, y) → (-x, -i*y)  [since 1/i = -i]

def PsiInv(P):
    if P.is_zero():
        return E2_2(0)
    xP, yP = P.xy()
    return E2_2(-xP, -i * yP)

def Psi(Pt):
    if Pt.is_zero():
        return E_2(0)
    xT, yT = Pt.xy()
    return E_2(-xT, i * yT)

# -----------------------------
# Pick random non-infinity P in TorsPts; test PsiInv and Psi∘PsiInv
# -----------------------------
# P must be a point on E_2 (not just E)
candidates = [P for P in torsion_r_2 if not P.is_zero()]
P = random.choice(candidates)

print("\nRandom non-infinity P on E(Fq_2):")
print("P =", P)

# Map P to the twist E'
Pt = PsiInv(P)
print("PsiInv(P) on E' =", Pt)

# Map back from E' to E
P_back = Psi(Pt)
print("Psi(PsiInv(P)) =", P_back)

print("Check Psi(PsiInv(P)) == P :", P_back == P)
