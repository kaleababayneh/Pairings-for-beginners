from sage.all import *

q = 7691
Fq = GF(q)


a = Fq(0)
b = Fq(1)

R = PolynomialRing(Fq, 'i')
i = R.gen()
f = i**2 + 1

E = EllipticCurve(Fq, [a, b])
Fq_2 = GF(q**2, name='i', modulus=f)
E_2 = EllipticCurve(Fq_2, [a, b])

print(E.order().factor())
print(E_2.order().factor())

P = E_2(2693, 4312)  
i_ext = Fq_2.gen()  # Get the generator of the extension field
Q = E_2(633*i_ext + 6145, 7372*i_ext + 109)

r = 641

print(P.weil_pairing(Q, r))
print(P.weil_pairing(Q, r)**r)

a = 403
b = 135

# print(a*P)
# print(b*Q)

# print((a * P).weil_pairing(Q, r))
# print(P.weil_pairing(Q, r)**a)

# print(P.weil_pairing(b * Q, r))
# print(P.weil_pairing(Q, r)**b)


# print((a * P).weil_pairing(b * Q, r))
# print(P.weil_pairing(Q, r)**(a*b))

# Get the abelian group structure of E_2
G = E_2.abelian_group()
print("Abelian group structure:", G)

# Get the abstract group element corresponding to P
P_abstract = G(P)

# Generate the subgroup <P> using the built-in submodule method
H = G.submodule([P_abstract])
print("Subgroup <P>:", H)
print("Order of subgroup:", H.order())