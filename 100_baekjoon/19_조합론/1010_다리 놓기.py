import sys

def cnt(a, b):
    mul = 1
    for i in range(a):
        mul *= b
        b -= 1

    div = 1
    for j in range(a, 0, -1):
        div *= j

    ans = mul // div
    return ans

t = int(sys.stdin.readline())

arr = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(cnt(a, b))

print(*arr, sep='\n')

