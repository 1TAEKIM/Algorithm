n, m = map(int, input().split())

s = []
for i in range(n):
    tmp = input()
    s.append(tmp)

cnt = 0
for i in range(m):
    tmp = input()
    if tmp in s:
        cnt += 1

print(cnt)