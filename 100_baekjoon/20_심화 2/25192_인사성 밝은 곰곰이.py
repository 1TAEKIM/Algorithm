import sys

n = int(sys.stdin.readline())

arr = []
ans = 0
for i in range(n):
    name = sys.stdin.readline().strip()
    # enter 경우
    if name == 'ENTER':
        ans += len(set(arr))
        arr = []

    # arr 이 비어있는 경우
    elif name != 'ENTER' and len(arr) == 0:
        arr.append(name)
    else:
        arr.append(name)

# 마지막 배열 안에 들어있는 원소 개수 더해주기
ans += len(set(arr))
print(ans)
