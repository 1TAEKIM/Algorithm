import sys

n = int(sys.stdin.readline())

stack = []

cmd = []
for i in range(n):
    tmp = sys.stdin.readline().strip()
    cmd.append(tmp)

# print(cmd)
for i in range(n):
    num = cmd[i]

    if num[0] == '1':
        # num[-1]로 할 경우에, 1 10이면 0만 추가됨!!
        stack.append(int(num[2:]))

    elif num == '2':
        if len(stack) > 0:
            # pop method는 시간 복잡도가 O(N)
            print(stack.pop())
        else:
            print(-1)

    elif num == '3':
        print(len(stack))

    elif num == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif num == '5':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

