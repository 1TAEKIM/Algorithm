n = int(input())

stack = []

for _ in range(n):
    num = input()

    if num[0] == '1':
        stack.append(int(num[-1]))

    elif num == '2':
        if len(stack) > 0:
            # pop method는 시간 복잡도가 O(N)
            print(stack.pop(-1))
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

