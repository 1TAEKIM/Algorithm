import sys

def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):

    return recursion(s, 0, len(s) - 1, 1)

t = int(sys.stdin.readline())

arr = []
for i in range(t):
    tar = sys.stdin.readline().strip()
    arr.append(tar)

ans = []
for i in range(t):
    ans.append(isPalindrome(arr[i]))

for x, y in ans:
    print(x, y)
