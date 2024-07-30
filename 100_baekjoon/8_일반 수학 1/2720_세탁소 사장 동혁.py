t = int(input())

changes = [25, 10, 5, 1]
arr = []
for i in range(t):
    tmp = int(input())
    ans = []

    for j in changes:
        ans.append(tmp // j)
        tmp = tmp % j

    print(*ans)


"""
*list 하면 리스트 풀린 상태로 반환
"""