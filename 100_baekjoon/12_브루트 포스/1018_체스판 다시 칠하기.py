n, m = map(int, input().split())

arr = []
for i in range(n):
    row = input()
    arr.append(list(row))

# 시작이 W 인 경우와 B 인 경우 모두 확인해야함.
def white_cnt(arr):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:
                if arr[i][j] != 'W':
                    cnt += 1

            elif i % 2 == 1 and j % 2 == 1:
                if arr[i][j] != 'W':
                    cnt += 1

            elif i % 2 == 0 and j % 2 == 1:
                if arr[i][j] != 'B':
                    cnt += 1

            elif i % 2 == 1 and j % 2 == 0:
                if arr[i][j] != 'B':
                    cnt += 1
    return cnt

def black_cnt(arr):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:
                if arr[i][j] != 'B':
                    cnt += 1

            elif i % 2 == 1 and j % 2 == 1:
                if arr[i][j] != 'B':
                    cnt += 1

            elif i % 2 == 0 and j % 2 == 1:
                if arr[i][j] != 'W':
                    cnt += 1

            elif i % 2 == 1 and j % 2 == 0:
                if arr[i][j] != 'W':
                    cnt += 1

    return cnt

result = []

for i in range(n - 7):
    for j in range(m - 7):
        tmp_arr = []
        for k in range(i, i + 8):
            tmp = []
            for l in range(j, j + 8):
                tmp.append(arr[k][l])

            tmp_arr.append(tmp)
        # print((tmp_arr))
        result.append(white_cnt(tmp_arr))
        result.append(black_cnt(tmp_arr))

print(min(result))