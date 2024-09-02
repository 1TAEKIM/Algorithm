n = int(input())

flag = 0
for i in range(n):
    char_i = str(i)
    tar = i
    for j in range(len(char_i)):
        tar += int(char_i[j])
    if tar == n:
        flag = 1
        print(i)
        break

if flag == 0: print('0')