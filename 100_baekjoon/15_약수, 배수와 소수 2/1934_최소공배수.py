t = int(input())

arr = []
for i in range(t):
    a, b = map(int, input().split())
    arr.append([a, b])

    while b != 0:
        r = a % b
        a = b
        b = r

    print(a)


# Project in progress