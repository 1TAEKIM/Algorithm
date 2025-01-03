def eucl(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

u = (a * d) + (b * c)
d = (b * d)
# print(u, d)

gcd = eucl(u, d)
if gcd == 1:
    print(u, d)
else:
    u = u // gcd
    d = d // gcd
    while gcd == 1:
        gcd = eucl(u, d)
        u = u // gcd
        d = d // gcd
    print(u, d)
