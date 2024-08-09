n = int(input())

dot = []
for i in range(n):
    a, b = map(int, input().split())
    dot.append(a)
    dot.append(b)

min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000
for i in range(n):
    if dot[2 * i] > max_x:
        max_x = dot[2 * i]
    if dot[2 * i] < min_x:
        min_x = dot[2 * i]
    if dot[2 * i + 1] > max_y:
        max_y = dot[2 * i + 1]
    if dot[2 * i + 1] < min_y:
        min_y = dot[2 * i + 1]

if n == 1: print(0)
else: print((max_x - min_x) * (max_y - min_y))