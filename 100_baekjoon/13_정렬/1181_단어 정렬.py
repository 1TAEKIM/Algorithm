n = int(input())

arr = []
for i in range(n):
    word = input()
    arr.append((len(word), word))

arr = list(set(arr))
# 알파벳 개수로 정렬
arr.sort()
# python은 길이로도 정렬하는 옵션이 존재
arr.sort(key=len)

for i in range(len(arr)):
    print(arr[i][1])