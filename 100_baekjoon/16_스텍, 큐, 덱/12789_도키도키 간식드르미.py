import sys

n = int(sys.stdin.readline())
arr = [int(i) for i in sys.stdin.readline().split()]

stack = []
i = 0
tar = 1
flag = 0
while arr:
    if arr[i] == tar:
        arr.pop(0)
        tar += 1
    else:
        if stack and stack[-1] == tar:
            stack.pop()
            tar += 1
        else:
            stack.append(arr.pop(0))

if stack:
    while stack:
        if stack[-1] == tar:
            stack.pop()
            tar += 1
        else:
            break
    if stack: print('Sad')
    else: print('Nice')
else:
    print('Nice')

