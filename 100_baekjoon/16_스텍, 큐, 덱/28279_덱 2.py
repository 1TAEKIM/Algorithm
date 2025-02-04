import sys
from collections import deque

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    tmp = sys.stdin.readline().strip()
    arr.append(tmp)

deq = deque()

for i in range(n):
    num = arr[i]

    if num[0] == '1':
        deq.appendleft(num[2:])
    elif num[0] == '2':
        deq.append(num[2:])
    elif num[0] == '3':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif num[0] == '4':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif num[0] == '5':
        print(len(deq))
    elif num[0] == '6':
        if deq:
            print(0)
        else:
            print(1)
    elif num[0] == '7':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif num[0] == '8':
        if deq:
            print(deq[-1])
        else:
            print(-1)
