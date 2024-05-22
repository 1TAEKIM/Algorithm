n = input()

ans = 0
for i in range(len(n)):
    if n[i] in 'ABC':
        ans += 3

    elif n[i] in 'DEF':
        ans += 4

    elif n[i] in 'GHI':
        ans += 5

    elif n[i] in 'JKL':
        ans += 6

    elif n[i] in 'MNO':
        ans += 7

    elif n[i] in 'PQRS':
        ans += 8

    elif n[i] in 'TUV':
        ans += 9

    elif n[i] in 'WXYZ':
        ans += 10

    else:
        ans += 11

print(ans)