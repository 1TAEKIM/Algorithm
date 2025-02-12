import sys

sen = []

for line in sys.stdin:
    # 개행 문자 제거
    line = line.rstrip()

    # '.' 만 있는 줄이 들어오면 입력 종료
    if line == '.':
        break

    # 문장 끝에 '.'가 있다면, '.'을 제외하고 리스트에 추가
    if line[-1] == '.':
        sen.append(line[:-1])
    else:
        sen.append(line)

for i in range(len(sen)):
    tar = sen[i]
    stack = []
    flag = 0
    for j in range(len(tar)):
        if tar[j] == '(' or tar[j] == '[':
            stack.append(tar[j])

        if tar[j] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 1
                break
        elif tar[j] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 1
                break

    if stack or flag == 1: print('no')
    else: print('yes')
