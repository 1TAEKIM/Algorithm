import sys

n = int(sys.stdin.readline())

arr = []
cnt = 0
for i in range(n):
    name = sys.stdin.readline().strip()
    # enter 경우
    if name == 'ENTER':
        arr = []
    # arr 이 비어있는 경우
    elif name != 'ENTER' and len(arr) == 0:
        arr.append(name)
        cnt += 1
    else:
        if name not in set(arr) and arr[-1] != name:
            arr.append(name)
            cnt += 1

print(cnt)
