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
print(list(E.order().factor()))
print(list(Ek.order().factor()))
print(cofactor)
print(E.is_supersingular())

set_of_points = set()
for i in Ek.points():
    set_of_points.add(r*i)
print("set_of_points", set_of_points)

# E(Fqk )/rE(Fqk).









# torsion_r = E(0).division_points(r)
# torsion_r_2 = Ek(0).division_points(r)

# print(torsion_r)
# print(torsion_r_2)

# # rmap = Ek.scalar_multiplication(r)
# # R = rmap(torsion_r_2[1])
# # print("rmap", rmap)
# # print("R", R)

# phi = Ek.scalar_multiplication(r)
# print("phi", phi)
# print("phi.rational_maps()", phi.rational_maps())

# # endomorphism that equal multiplication by 3
# phi = Ek.scalar_multiplication(3)
# Xmap, Ymap = phi.rational_maps()

# S = Ek.random_point()
# while S == Ek(0):
#     S = Ek.random_point()
# xS, yS = S.xy()
# image_by_maps = (Xmap(x=xS, y=yS), Ymap(x=xS, y=yS))
# image_by_group = (3*S).xy()


# # kernel points (Ek-rational)
# ker_pts = Ek(0).division_points(r)   # points T with r*T = O in Ek
# print("kernel points (Ek-rational):", ker_pts)
# print("size:", len(ker_pts))

# # sanity check
# print(all(phi(T).is_zero() for T in ker_pts))


# tors = [T for T in ker_pts if not T.is_zero()]

# # Find two points that generate E2[r] (rank-2 over Z/rZ)
# P = tors[0]
# Q = None
# for T in tors[1:]:
#     # "independent" here means T is not in <P>
#     if not any(T == k*P for k in range(r)):
#         Q = T
#         break

# print("Chosen generators P, Q:", P, Q)


# # iso_P = Ek.isogeny(P)
# # print("\nIsogeny with kernel <P>: iso_P =", iso_P)


# # # For a cyclic isogeny with kernel <Q> of order r:
# # iso_Q = Ek.isogeny(Q)
# # print("\nIsogeny with kernel <Q>: iso_Q =", iso_Q)


# points = Ek.points()

# phi = Ek.scalar_multiplication(r)
# coset_set = { phi(P) for P in points }
# coset_list = list(coset_set)
# print("coset_list", coset_list)

# # def flower_generator(tors_pts):

# #     V = set()
# #     S = set(tors_pts)
# #     petals = int(len(S)**0.5) + 1  # sqrt(#S) + 1
# #     pts_in_pet = petals - 1
# #     T = []
    
# #     for _ in range(petals):
# #         S = S - V
# #         if not S:
# #             break
# #         candidates = [P for P in S if not P.is_zero()]
# #         if not candidates:
# #             break
# #         P = random.choice(candidates)
# #         # Generate the petal: {1*P, 2*P, ..., (petals-1)*P}
# #         V = set(j * P for j in range(1, pts_in_pet + 1))
# #         T.append(V)
    
# #     return T


# # petals = flower_generator(torsion_r_2)


# # print("\n--- Flower Generator 1 ---")
# # for idx, petal in enumerate(petals):
# #     print(f"Petal {idx+1}: {(petal)}")

