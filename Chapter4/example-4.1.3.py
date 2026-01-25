from sage.all import *
import random

q = 11
Fq = GF(q)

a = Fq(7)
b = Fq(2)

# Define extension field Fq3 with modulus x^3 + x + 4
R = PolynomialRing(Fq, 'x')
x = R.gen()
f = x**3 + x + 4  # Same modulus as Magma
Fq3 = GF(q**3, name='u', modulus=f)
u = Fq3.gen()

E = EllipticCurve(Fq, [a, b])
E3 = EllipticCurve(Fq3, [a, b])

r = 7

print("Order factorization E(Fq):", list(E.order().factor()))
print("Order factorization E(Fq3):", list(E3.order().factor()))

# Get r-torsion points
torsion_pts = set(E3(0).division_points(r))
print(f"\nNumber of {r}-torsion points:", len(torsion_pts))



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
petals = flower_generator(torsion_pts)

for i, petal in enumerate(petals):
    print(f"Petal {i+1}: {len(petal)}")



def frobenius(P):
    """
    Apply the q-th power Frobenius map to a point P on E(Fq3).
    Raises the coordinates to the q-th power.
    """
    if P.is_zero():
        return P
    x, y = P.xy()
    return P.curve()(x**q, y**q)


def trace_map(P):
    """
    Compute the trace map: Tr(P) = pi^2(P) + pi(P) + P
    where pi is the Frobenius map.
    """
    pi_P = frobenius(P)
    pi2_P = frobenius(pi_P)
    return pi2_P + pi_P + P


print("\n--- Trace Map Examples ---")

# Test with points using the generator u
# In Magma, u^k means u raised to power k, which is an element of Fq3
# We need to find points on E3 and test the trace map

# Get a point from the torsion and test
test_points = [P for P in torsion_pts if not P.is_zero()]
if test_points:
    P = test_points[0]
    print(f"P = {P}")
    print(f"TraceMap(P) = {trace_map(P)}")

# You can also manually specify points if needed:
# Example: P = E3([u^481, u^1049]) in Magma notation
# In SageMath: P = E3(u**481, u**1049)
try:
    P1 = E3(u**481, u**1049)
    print(f"\nP1 = E3(u^481, u^1049) = {P1}")
    print(f"TraceMap(P1) = {trace_map(P1)}")
except:
    print("\nP1 = E3(u^481, u^1049) is not on the curve")

try:
    Q1 = E3(u**423, u**840)
    print(f"\nQ1 = E3(u^423, u^840) = {Q1}")
    print(f"TraceMap(Q1) = {trace_map(Q1)}")
except:
    print("\nQ1 = E3(u^423, u^840) is not on the curve")

try:
    R1 = E3(u**1011, u**1244)
    print(f"\nR1 = E3(u^1011, u^1244) = {R1}")
    print(f"TraceMap(R1) = {trace_map(R1)}")
except:
    print("\nR1 = E3(u^1011, u^1244) is not on the curve")
