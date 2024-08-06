m = int(input())
n = int(input())

num = []
for i in range(m, n + 1):
    flag = 0
    if i == 1:
        flag = 1
        continue
    for j in range(2, i + 1):
        if j != i and i % j == 0:
            flag = 1
            break

    if flag == 0: num.append(i)

if len(num) == 0: print('-1')
else:
    print(sum(num))
    print(num[0])
