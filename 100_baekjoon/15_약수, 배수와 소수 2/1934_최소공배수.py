def euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())

arr = []
for i in range(t):
    a, b = map(int, input().split())
    arr.append([a, b])

# 유클리드 호제법 공부 필요!!
for i in range(t):
    gcd = euclidean(arr[i][0], arr[i][1])
    print(arr[i][0] * arr[i][1] // gcd)
