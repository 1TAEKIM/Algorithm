import sys

t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    tmp = sys.stdin.readline().strip()
    arr.append(tmp)


for i in range(t):
    flag = 0
    tar = list(arr[i])
    if tar[-1] == '(':
        flag = 1
    else:
        ans = []
        for j in range(len(tar)):
            if tar[-1] == ')':
                ans.append(tar.pop())
            else:
                if ans:
                    tar.pop()
                    ans.pop()
                else:
                    flag = 1
                    break

    if flag == 1 or ans: print('NO')
    else: print('YES')