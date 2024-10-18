n = int(input())

arr = []
for i in range(n):
    word = input()
    arr.append((len(word), word))

arr = list(set(arr))
# 알파벳 개수로 정렬
arr.sort()

