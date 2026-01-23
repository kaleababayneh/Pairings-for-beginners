from sage.all import *

# NIST P-256
p = Integer(2)**256 - Integer(2)**224 + Integer(2)**192 + Integer(2)**96 - 1
r = Integer(115792089210356248762697446949407573529996955224135760342422259061068512044369)
b = Integer(41058363725152142129326129780047268409114441015993725554835256314039467401291)

Fp = GF(p)
E  = EllipticCurve(Fp, [-3, Fp(b)])
O  = E(0)

Gx = Integer(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296)
Gy = Integer(0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
P  = E(Fp(Gx), Fp(Gy))

Hx = Integer(53987601597021778433910548064987973235945515666715026302948657055639179420355)
Hy = Integer(53690949263410447908824456005055253553237881490194075871737490561466076234637)
H  = E(Fp(Hx), Fp(Hy))

print("E =", E)
print("P on curve?", P in E)
print("H on curve?", H in E)

# Fast, meaningful checks (avoid E.order() for a 256-bit curve)
print("r*P == O ?", r*P == O)
print("P != O ?", P != O)

# Because r is prime, these two imply ord(P) = r
print("Therefore ord(P) = r (since r is prime):", (r*P == O) and (P != O))
