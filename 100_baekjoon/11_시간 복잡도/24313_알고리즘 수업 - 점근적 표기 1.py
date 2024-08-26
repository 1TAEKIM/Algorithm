a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# n0을 대입 했을 때 식 만족하면 됨. 조건 생각!!

flag = 0
for n in range(n0, 100):
    if a1 * n + a0 <= c * n:
        continue
    else:
        flag = 1
        break

if flag == 1: print('0')
else: print('1')