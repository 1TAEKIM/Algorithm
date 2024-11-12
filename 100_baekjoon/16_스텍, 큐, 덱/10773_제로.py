k = int(input())

arr = []
ans = 0
for i in range(k):
    num = int(input())
    if len(arr) == 0 and num == 0:
        continue
    elif num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))

