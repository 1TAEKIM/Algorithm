# 각 창문 번호의 약수의 개수가 짝수 0, 홀수 1
# 약수의 개수 구하기
"""
1부터 n의 제곱근 까지의 수로 나눠서 약수를 구한 후
그 약수를 가지고 n을 다시 나눈 후 중복 제거 
=> 시간 복잡도가 O(N)에서 O(√N)으로 됨
"""

# 제곱근
def sqt(n):
    tmp = []
    sq = int(n ** 1//2)
    for i in range(1, sq + 1):
        if n % i == 0:
           tmp.append(i)

    for i in range(len(tmp)):
        tmp1 = n % tmp[i]
        if tmp1 == 0:
           tmp.append(tmp1)
    re = len(set(tmp))

    return re

n = int(input())

arr = []
ans = 1
for i in range(1, n):
    tmp = sqt(i + 1)

    if tmp % 2 == 1:
        ans += 1

print(ans)
