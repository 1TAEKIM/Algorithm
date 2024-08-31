n = input()

n = list(n)
n = sorted(n, reverse=True)

for i in range(len(n)):
    print(n[i], end='')