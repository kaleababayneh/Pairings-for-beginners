from sage.all import *

p = 1021
Fq = GF(p)

a = Fq(905)
b = Fq(100)

E = EllipticCurve(Fq, [a, b])
n = E.order()

P = E(1006, 416)
Q = E(612, 827)
O = E(0)


print("#E(Fq) =", n)
print("factor(#E) =", factor(n))
print("P =", P)
print("Q =", Q)

prime_factors = [pr for (pr, exp) in factor(n)]
print("Prime factors:", prime_factors)

# --- Compute subgroup projections and solve each tiny DLP by brute force ---
ks = []
mods = []

for j in prime_factors:
    h = n // j  # cofactor
    Pj = h * P
    Qj = h * Q

    print("\n--- j =", j, "h =", h, "---")
    print("Pj =", Pj)
    print("Qj =", Qj)

    # Solve Qj = kj * Pj in subgroup of size j
    # Must allow kj = 0..j-1
    kj = None
    for t in range(j):  # j is a Sage Integer, range works fine
        if t * Pj == Qj:
            kj = t
            break

    if kj is None:
        raise RuntimeError(f"No solution found mod {j}. (This should not happen if P generates the right subgroup.)")

    print("Found kj =", kj, "(mod", j, ")")
    ks.append(Integer(kj))
    mods.append(Integer(j))

print("\nCongruences: k ≡ ks[i] (mod mods[i])")
for r, m in zip(ks, mods):
    print(f"k ≡ {r} (mod {m})")

# --- CRT recombination ---
k = crt(ks, mods)           # solution modulo product(mods) = n (since these are coprime primes)
k = Integer(k % n)          # normalize to 0..n-1

print("\nCRT solution k =", k, "(mod", n, ")")
print("Check: k*P == Q ?", (k * P == Q))
print("k*P =", k * P)
print("Q   =", Q)
