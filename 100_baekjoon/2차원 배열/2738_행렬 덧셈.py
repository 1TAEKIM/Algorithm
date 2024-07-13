N, M = map(int, input().split())

a = []
b = []

for i in range(N):
    s = list(map(int, input().split()))
    a.append(s)

for i in range(N):
    s = list(map(int, input().split()))
    b.append(s)



for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end=' ')

    print()

