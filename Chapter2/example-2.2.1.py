from sage.all import *

p = 101
Fp = GF(p)
E = EllipticCurve(Fp, [1, 1])

order = E.order()
order_divisors = order.divisors()
print(E)
#print("Points on E:", E.points())
print("Order of E:", order)
print("Order divisors:", order_divisors)
P =E(47,12)


for i in order_divisors:
    print(i*P)


# orders = []
# for i in range(1, order + 1):
#     orders.append(order(E.points()[i]))
# print(orders)
