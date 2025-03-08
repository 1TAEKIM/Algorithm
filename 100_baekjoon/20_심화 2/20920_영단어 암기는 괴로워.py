"""
1. 자주 나오는 단어
2. 단어가 길수록
3. 알파벳 사전 순
반대로 해야지 최종 정렬
"""
import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
for i in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < m:
        continue
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

dic = sorted(dic.items(), key=lambda x:x[0])
dic = sorted(dic, key=lambda x:len(x[0]), reverse=True)
dic = sorted(dic, key=lambda x:x[1], reverse=True)

for i in dic:
    print(i[0])
