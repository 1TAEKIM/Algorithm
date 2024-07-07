N = int(input())

word = []
for i in range(N):
    a = input()
    word.append(a)

# 뒤에 앞에 나왔던 단어가 나오면 안된다
# 단어 돌면서 리스트에 저장 -> 검사

cnt = 0
for i in range(len(word)):
    flag = 0
    check = []
    for j in range(len(word[i])):
        if word[i][j] not in check:
            check.append(word[i][j])
        else:
            if check[-1] != word[i][j]:
                flag = 1
                break

    if flag == 0: cnt += 1

print(cnt)