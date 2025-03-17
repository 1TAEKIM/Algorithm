import sys

def draw_stars(n):
    if n == 1:
        return ['*']

    stars = draw_stars(n // 3)
    arr = []

    for i in stars:
        arr.append(i * 3)
    for i in stars:
        arr.append(i + ' ' * (n // 3) + i)
    for i in stars:
        arr.append(i * 3)

    return arr

n = int(sys.stdin.readline())
print('\n'.join(draw_stars(n)))
