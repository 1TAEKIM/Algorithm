n = int(input())
tar = []
for i in range(n):
    tmp = int(input())
    tar.append(tmp)

tar = sorted(tar)
for i in range(len(tar)):
    print(tar[i])