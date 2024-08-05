n = int(input())

i = 2
while True:
    if n == 1:
        break

    if n % i == 0 and n != 1:
        n = n / i
        print(i)
        i = 2
    else:
        i += 1