import sys

n = int(sys.stdin.readline())

x = 1
y = 1

cnt = 1
while True:
    if cnt == n: break
    if x == 1:
        old_y = y
        y += 1
        cnt += 1
        if cnt == n: break

        for _ in range(y - 1):
            x += 1
            y -= 1
            cnt += 1
            if cnt == n: break

    elif y == 1:
        x += 1
        cnt += 1
        if cnt == n: break
        for _ in range(x - 1):
            x -= 1
            y += 1
            cnt += 1
            if cnt == n: break

print(f'{x}/{y}')