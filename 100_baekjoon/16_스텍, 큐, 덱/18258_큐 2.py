import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque()
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        deq.append(int(order[1]))

    elif order[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)

    elif order[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif order[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)


