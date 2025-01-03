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
    print(u, d)

# !! 기약분수는 분모와 분자를 각각 최대공약수로 나눈 값 !! #
