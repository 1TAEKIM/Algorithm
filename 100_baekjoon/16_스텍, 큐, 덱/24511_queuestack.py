import sys
from collections import deque

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))

deq = deque()

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if a[i] == 0:
        deq.append(b[i])

for i in range(m):
    deq.appendleft(c[i])
    print(deq.pop(), end= ' ')