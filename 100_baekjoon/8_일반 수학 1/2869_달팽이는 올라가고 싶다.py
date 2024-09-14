import sys

# a = 올라갈 수 있는 거리, b = 미그러지는 거리, v = 나무막대 높이
a, b, v = map(int, sys.stdin.readline().split())
# v - b = 올라가야할 거리
# a - b = 하루에 갈 수 있는 거리
#올라가야할 거리 % 하루에 갈 수 있는 거리 == 0

if (v - b) % (a - b) == 0:
    print((v-b) // (a-b))
else:
    print((v-b) // (a-b) + 1)