import sys

n = int(sys.stdin.readline())

arr = []
cnt = 0
for i in range(n):
    a, b = sys.stdin.readline().split()
    if len(arr) == 0:
        arr.append(a)
        arr.append(b)
        cnt += 2

    else:
        if arr[-1] == a:
            arr.append(b)
            cnt += 1


print()
# 머릿 속 복잡