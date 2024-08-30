arr = []
for i in range(5):
    n = int(input())
    arr.append(n)

arr = sorted(arr)
print(sum(arr) // 5)
print(arr[2])