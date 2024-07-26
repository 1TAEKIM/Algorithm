alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
ans = 0
for i, num in enumerate(n[::-1]):
    ans += (int(b) ** i) * (alp.index(num))
print(ans)

"""
파이썬의 int 함수는 임의의 진버 수를 10진법으로 변환하는데 사용할 수 있음
아래의 코드는 위 문제의 답과 동일한 결과
n, b = input().split()
print(int(n, int(b)))
"""
