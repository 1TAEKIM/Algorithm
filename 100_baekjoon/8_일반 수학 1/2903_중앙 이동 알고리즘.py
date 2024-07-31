n = int(input())

tmp = 2
for i in range(n):
    tmp += 2 ** i

print(tmp * tmp)