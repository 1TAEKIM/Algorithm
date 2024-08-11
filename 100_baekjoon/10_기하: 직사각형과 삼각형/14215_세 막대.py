a, b, c = map(int, input().split())

num = [a, b, c]
num = sorted(num)

if num[2] < (num[0] + num[1]):
    print(num[0] + num[1] + num[2])
elif num[2] == (num[0] + num[1]):
    print(num[0] + num[1] + (num[2] - 1))
elif num[2] > (num[0] + num[1]):
    print((num[0] + num[1]) * 2 - 1)
