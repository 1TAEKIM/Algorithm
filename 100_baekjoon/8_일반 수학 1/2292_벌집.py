# 1, 2 - 7, 8 - 19, 20 - 37, 38 - 64

n = int(input())
num = 1
cnt = 1
i = 1
while True:
    if num >= n:
        break
    else:
        cnt += 1
        num += (6 * i)
        i += 1

if n == 1: print(1)
else: print(cnt)