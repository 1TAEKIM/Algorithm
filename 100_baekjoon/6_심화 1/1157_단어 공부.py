target = input()

target = target.upper()

dict = {}

for i in range(len(target)):
    if target[i] not in dict.keys():
        dict[target[i]] = 1

    else:
        dict[target[i]] += 1

# 맥스값이 2개 이상이면 '?' 출력, 1개면 value 값에 해당하는 key 출력

values = list(dict.values())

cnt = 0
for i in range(len(values)):
    if max(values) == values[i]:
        cnt += 1

if cnt >= 2: print('?')
else:
    for k, v in dict.items():
        if v == max(values):
            print(k)
