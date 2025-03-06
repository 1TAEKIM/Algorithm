import sys

n = int(sys.stdin.readline())

arr = ['ChongChong']
cnt = 0
for i in range(n):
    a, b = sys.stdin.readline().split()
    if a in arr:
        arr.append(b)
    elif b in arr:
        arr.append(a)

print(len(set(arr)))
