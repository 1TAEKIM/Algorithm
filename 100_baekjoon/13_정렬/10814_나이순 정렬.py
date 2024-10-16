n = int(input())

arr = []
eql = []
for i in range(n):
    tmp = list(input().split())
    arr.append(tmp)
    if arr[i - 1][0] == arr[i][0]:
       eql.append(tmp)

arr = sorted(arr)

