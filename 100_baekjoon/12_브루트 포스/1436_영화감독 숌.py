n = int(input())

cnt = 0
tar = 0
while True:
    tmp_cnt = 0
    if cnt == n:
        print(tar)
        break
    tar += 1
    tmp_tar = str(tar)
    for i in range(len(tmp_tar) - 2):
        if tmp_tar[i] == '6' and tmp_tar[i + 1] == '6' and tmp_tar[i + 2] == '6':
            tmp_cnt += 1
    if tmp_cnt != 0:
        cnt += 1
