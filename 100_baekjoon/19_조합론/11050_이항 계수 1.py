import sys

n, k = map(int, sys.stdin.readline().split())

ans = 1
for i in range(k):
    ans *= n
    n -= 1

div = 1
for j in range(1, k + 1):
    div *= j


print(ans//div)