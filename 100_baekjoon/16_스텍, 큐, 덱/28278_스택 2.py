n = int(input())

stack = []
for i in range(n):
    num = int(input())
    if num == 1:
        stack.append(num)
    elif num == 2:
        if len(stack) == 0:
            print(-1)
        else:
            for j in range(len(stack) - 1):
                print(stack[j])
    elif num == 3:
        print(len(stack))
    elif num == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

