while True:
    n = int(input())
    if n == -1:
        break

    ans = []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)
    if sum(ans) == n:
        print(n, '= ', end='')
        for i in range(len(ans)):
            if i == len(ans) - 1:
                print(ans[i])
            else:
                print(ans[i], end=' + ')

    else:
        print(f'{n} is NOT perfect.')