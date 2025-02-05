import sys
from collections import deque

n = int(sys.stdin.readline())

ar = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append([i + 1, ar[i]])

deq = deque(arr)

ans = []
while deq:
    tmp = deq.popleft()
    ans.append(tmp[0])

    if tmp[1] > 0:
        deq.rotate(-(tmp[1] - 1))
    else:
        deq.rotate(-tmp[1])

print(*ans)
