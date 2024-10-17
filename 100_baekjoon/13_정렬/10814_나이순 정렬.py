n = int(input())

arr = []

for i in range(n):
    age, name = map(str, input().split())
    arr.append((int(age), name))

# (age, name)에서 age만 비교
arr.sort(key= lambda x : x[0])

for i in arr:
    print(i[0], i[1])