word = input()

n = len(word)
arr = []

for i in range(n):
    for j in range(n - i):
        arr.append(word[j:j+i+1])

print((len(set(arr))))
