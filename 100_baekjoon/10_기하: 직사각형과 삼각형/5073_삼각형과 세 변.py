# 삼각형 조건: 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길어야 된다.

while True:
    a, b, c = map(int, input().split())
    tmp = [a, b, c]
    if a == 0 and b == 0 and c == 0:
        break

    tmp = sorted(tmp)

    if tmp[2] >= tmp[0] + tmp[1]:
        print('Invalid')
    elif a == b and a == c and b == c:
        print('Equilateral')
    elif a != b and a != c and b != c:
        print('Scalene')
    else:
        print('Isosceles')