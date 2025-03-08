import sys

n = int(sys.stdin.readline())

dic = {}
arr = []
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

a_sum = 0
for i in range(len(arr)):
    a_sum += arr[i]
# 산술평균
print(round(a_sum / len(arr)))

# 중앙값
arr.sort()
print(arr[len(arr) // 2])

# 최빈값
c = sorted(dic.items(), key=lambda x:x[0])
c = sorted(c, key=lambda x:x[1], reverse=True)
if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

# 범위
d = list(dic.keys())
d = sorted(d)
print(d[-1] - d[0])
