n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input())

tar = []
for i in range(m):
    tar.append(input())

ans = []
cnt = 0
for i in range(m):
    if tar[i] in arr:
        ans.append(tar[i])
        cnt += 1

ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])



