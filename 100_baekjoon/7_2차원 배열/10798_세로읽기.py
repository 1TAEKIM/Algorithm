arr = []
arr_max = 0

for i in range(5):
    s = list(input())
    arr.append(s)
    if len(s) > arr_max:
        arr_max = len(s)

# 첫 번째 행이 최대 길이가 아닐 경우 오류 발생
for i in range(arr_max):
    for j in range(5):
        if i >= len(arr[j]):
            continue
        else:
            print(arr[j][i], end='')
