n = int(input())

num = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if num[i] == 1: continue
    flag = 0
    for j in range(2, num[i]):
        if num[i] % j == 0:
            flag = 1
            break

    if flag == 0: cnt += 1

print(cnt)