import sys

E, S, M = map(int, sys.stdin.readline().split())
ans = 0
e, s, m = 0, 0, 0
while True:
    e += 1
    s += 1
    m += 1
    ans += 1

    # 범위 벗어날 경우 다시 시작
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

    if e == E and s == S and m == M:
        print(ans)
        break

