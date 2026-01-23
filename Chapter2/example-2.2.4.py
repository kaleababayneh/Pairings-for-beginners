from sage.all import *

q = 23
Fq = GF(q)

low  = q + 1 - floor(2*sqrt(q))
high = q + 1 + floor(2*sqrt(q))
size = high - low  # so number of possible orders is size+1

print("q =", q)
print("Hasse interval: [low, high] =", (low, high))
print("Possible #E(Fq) values:", size + 1)

curves = []
orders = set()          # for fast membership testing
orders_list = []        # to preserve insertion order (optional)

# Nonsingularity condition for short Weierstrass in char != 2,3:
# discriminant != 0  <=> 4a^3 + 27b^2 != 0 in Fq
def is_nonsingular(a, b):
    return (4*a**3 + 27*b**2) != 0

# Keep sampling until we have size+1 distinct orders
while len(curves) < (size + 1):
    a = Fq.random_element()
    b = Fq.random_element()

    if not is_nonsingular(a, b):
        continue

    E = EllipticCurve(Fq, [a, b])
    n = E.order()

    if n not in orders:
        curves.append(E)
        orders.add(n)
        orders_list.append(n)
        print(f"Found new order {n}: E: y^2 = x^3 + ({a})x + ({b})   (total={len(curves)})")

print("\nCurves (one per distinct order):")
for i, E in enumerate(curves, start=1):
    a, b = E.a4(), E.a6()  # for short Weierstrass these correspond to a and b
    print(f"{i:2d}. a={a}, b={b}, #E(Fq)={E.order()}")

print("\nOrders:")
print(orders_list)
