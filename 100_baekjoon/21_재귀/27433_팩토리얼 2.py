import sys

n = int(sys.stdin.readline())

def fac(num):
    if num == 1:
        return 1

    else:
        return num * fac(num - 1)

if n == 0: print(1)
else: print(fac(n))
