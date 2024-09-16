n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])

# y좌표가 증가하는 순서, y좌표가 같으면 x좌표가 증가하는 순서
b = sorted(arr)

for i in range(n):
    print(b[i][1], b[i][0])