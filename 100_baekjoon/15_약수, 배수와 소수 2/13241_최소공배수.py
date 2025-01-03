def euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# 유클리드 호제법 공부 필요!!
a, b = map(int, input().split())
print(a * b // euclidean(a, b))
