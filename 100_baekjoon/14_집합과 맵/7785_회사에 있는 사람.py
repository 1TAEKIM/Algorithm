n = int(input())

_dict = {}

for i in range(n):
    name, info = input().split()
    _dict[name] = info

    if info == 'leave':
        _dict.pop(name)

ans = sorted(_dict.keys(), reverse=True)

for i in range(len(ans)):
    print(ans[i])
