import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque([i for i in range(1, n + 1)])

while deq:
    if len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    else:
        print(*deq)
        break
