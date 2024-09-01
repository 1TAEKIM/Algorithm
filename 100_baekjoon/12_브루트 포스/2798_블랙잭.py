n, m = map(int, input().split())

arr = []
arr = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    sum = 0
    for j in range(i + 1, n - 1):
        sum = arr[i]
        for k in range(j + 1, n):
            sum = arr[i] + arr[j]
            sum += arr[k]
            if ans < sum <= m:
                ans = sum

print(ans)
