a, b = map(int, input().split())
arr = []
if a > b:
    while True:
        if a % b == 0:
            print(b)
            break
        else:
            re = a % b
            a = b
            b = re
