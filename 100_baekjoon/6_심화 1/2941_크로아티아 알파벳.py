target = input()

word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# word를 *로 변경한 후, 총 개수 세기
for i in word:
    target = target.replace(i, "*")

print(len(target))