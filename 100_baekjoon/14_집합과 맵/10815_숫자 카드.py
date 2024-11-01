import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
# 시간 초과 풀이
for i in range(m):
    if m_arr[i] in n_arr:
        print(1, end=' ')
    else:
        print(0, end=' ')
