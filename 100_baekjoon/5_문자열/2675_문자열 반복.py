def output(R, S):
    ans = []
    for i in range(len(S)):
        for _ in range(int(R)):
            ans.append(S[i])

    return ans


T = int(input())

for _ in range(T):
    R, S = input().split()
    ans = output(R, S)
    for i in range(len(ans)):
        print(ans[i], end='')
    print()
