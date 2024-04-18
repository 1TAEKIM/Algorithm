# 10811번: 바구니 뒤집기

"""
M 번 바구니의 순서를 역순으로
"""
# N개의 바구니를 M번 순서 바꾸기
N, M = map(int, input().split())
ans = [i for i in range(1, N+1)]


for k in range(M):
    i, j = map(int, input().split())
    tmp = ans[i - 1:j]
    tmp.reverse()
    ans[i - 1:j] = tmp

for i in range(len(ans)):
    print(int(ans[i]), end=' ')