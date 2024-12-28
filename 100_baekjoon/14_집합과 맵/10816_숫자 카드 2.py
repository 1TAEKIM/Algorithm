n = int(input())
arr = list(map(int, input().split()))

_dict = {}
for i in range(n):
    if arr[i] not in _dict:
        _dict[arr[i]] = 1
    else:
        _dict[arr[i]] = _dict[arr[i]] + 1

# print(_dict)

m = int(input())
tar = list(map(int, input().split()))
for i in range(m):
    if tar[i] not in _dict:
        print(0, end=' ')
    else:
        print(_dict[tar[i]], end=' ')
