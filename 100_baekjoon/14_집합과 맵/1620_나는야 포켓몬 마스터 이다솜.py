"""
도감 N, 문제의 개수 M이 주어짐
포켓몬 이름은 영어, 첫 글자만 대문자, 일부는 마지막 문자만 대문자

문제가 알파벳이면 포켓몬 번호를
숫자로만 들어오면 포켓몬 번호에 해당하는 문자를
"""

n, m = map(int, input().split())

_dict = {}
for i in range(n):
    name = input()
    _dict[name] = i + 1

keys = list(_dict.keys())
values = list(_dict.values())

arr = []
for i in range(m):
    tar = input()
    arr.append(tar)

for i in range(m):
    if '0' <= arr[i][0] <= '9':
        idx = int(arr[i])
        print(keys[idx - 1])
    else:
        print(_dict[arr[i]])
