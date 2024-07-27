num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int, input().split())
ans = []
while True:
    if n < b:
        ans.append(n)
        break
    tar = n % b
    ans.append(tar)
    n = n // b

for i, num in enumerate(ans[::-1]):
    print(num_list[num], end='')