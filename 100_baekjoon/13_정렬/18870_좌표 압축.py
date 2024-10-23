n = int(input())
# 입력
arr = list(map(int, input().split()))

# 압축한 결과값은
# X1 > X2를 만족하는 서로 다른 좌표 X2의 개수와 같아야함
ans = arr
arr = list(set(arr))
arr.sort()

tmp = {}
for i in range(len(arr)):
    tmp[arr[i]] = i

# print(tmp)
for i in range(n):
    print(tmp[ans[i]], end=' ')
