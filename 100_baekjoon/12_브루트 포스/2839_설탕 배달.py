n = int(input())

# 5a + 3b = n

lim_a = n // 5
arr = []
flag = 0
for i in range(lim_a + 1):
    for j in range(n + 1):
        if 5 * i + 3 * j == n:
            flag = 1
            arr.append(i + j)
if flag == 1:
    print(min(arr))
else: print('-1')