import sys

n = int(sys.stdin.readline())

def pi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return pi(num - 1) + pi(num - 2)

print(pi(n))
