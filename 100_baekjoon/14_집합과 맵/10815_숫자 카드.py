n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

# dict가 비교할 때 list보다 훨씬 빠름!!
tmp = {}

for i in range(n):
    tmp[n_arr[i]] = 0

for i in range(m):
    if m_arr[i] in tmp:
        print(1, end=' ')
    else:
        print(0, end=' ')
