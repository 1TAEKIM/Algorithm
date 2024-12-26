"""
N개의 줄에 걸쳐 듣도 못한 사람의 이름과
N+2째 줄부터 보도 못한 사람의 이름이 주어진다.
"""
# 듣보잡의 수와 그 명단을 사전순으로 출력

n, m = map(int, input().split())

_dict = {}
ans = []
for i in range(n + m):
    name = input()
    if name not in _dict:
        _dict[name] = 0
    else:
        _dict[name] = 1
        ans.append(name)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

