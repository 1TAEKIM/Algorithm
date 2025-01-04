"""
모두 같은 간격, 가장 적은 나무
"""
# 주어진 간격의 최대공약수가 간격 되어야함
def euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

arr_dit = 1000000000
a = arr[1] - arr[0]
b = arr[2] - arr[1]
first_dit = euclid(a, b)

for i in range(n - 2):
    c = arr[i + 2] - arr[i + 1]
    tmp_dit = euclid(first_dit, c)
    if arr_dit > tmp_dit:
        arr_dit = tmp_dit

# print(arr_dit)

cnt = 0
for i in range(n - 1):
    tmp = arr[i + 1] - arr[i]
    cnt += (tmp // arr_dit) - 1

print(cnt)

# 아래 반례가 있어서 안됐음,
# 최대공약수가 1인 경우 생각했지만, 코드를 잘못 구성함(직전값과만 비교했었음)

# 4, 1, 8, 43, 48