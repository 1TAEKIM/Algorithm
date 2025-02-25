import sys

# 약수의 개수
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 2부터 큰 약수만 입력 받음
print(min(arr) * max(arr))
