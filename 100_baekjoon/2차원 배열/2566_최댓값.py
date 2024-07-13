arr = []
for i in range(9):
    s = list(map(int, input().split()))
    arr.append(s)

max = arr[0][0]
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            row = i
            col = j

print(max)
print(row + 1, col + 1, end=' ')