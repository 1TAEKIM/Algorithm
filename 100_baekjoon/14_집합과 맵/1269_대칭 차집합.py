import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# 교집합을 찾아서, a 에서 빼고, b 에서 빼기
cro = []
for i in range(n):
    if a[i] in b:
        cro.append(a[i])

for i in range(n):
    if a[i] in cro:
        a[i] = -1
cnt_a = 0
for i in range(n):
    if a[i] > 0:
        cnt_a += 1


for i in range(m):
    if b[i] in cro:
        b[i] = -1

cnt_b = 0
for i in range(m):
    if b[i] > 0:
        cnt_b += 1

print(cnt_a + cnt_b)
