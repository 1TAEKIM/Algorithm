# !! 몬테칼로 적분법

N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        x_idx = i
        for j in range(y, y + 10):
            y_idx = j

            if arr[x_idx][y_idx] == 0:
                arr[x_idx][y_idx] = 1

arr_sum = 0
for i in range(100):
    arr_sum += sum(arr[i])

print(arr_sum)