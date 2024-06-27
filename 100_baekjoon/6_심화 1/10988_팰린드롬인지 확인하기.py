"""
홀수면 + 1 / 2 짝수면 / 2
"""

target = input()
flag = 0
j = -1
if len(target) % 2 == 1:
    for i in range((len(target) + 1) // 2):
        if target[i] != target[j]:
            flag = 1
            break
        j -= 1

else:
    for i in range(len(target) // 2):
        if target[i] != target[j]:
            flag = 1
            break
        j -= 1

if flag == 0: print('1')
else: print('0')