import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

print(len(set(a) - set(b)) + len(set(b) - set(a)))
