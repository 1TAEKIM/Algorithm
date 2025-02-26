import sys

n = int(sys.stdin.readline())

"""
입력받을 때 배열 안에 있으면 카운트
"""
stack = []
cnt = 1
for i in range(n):
    a, b = sys.stdin.readline().split()
    if stack[-1] == b:
        cnt += 1

