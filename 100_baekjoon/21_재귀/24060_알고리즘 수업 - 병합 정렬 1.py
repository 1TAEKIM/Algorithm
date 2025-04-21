import sys

# 병합 정렬로 오름차순, 배열에 k번째 저장되는 수

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2 # q는 p, r의 중간 지점
        merge_sort(a, p, q) # 전반부 정렬
        merge_sort(a, q + 1, r) # 후반부 정렬
        merge(a, p, q, r) # 병합

def merge(a, p, q, r):
    global cnt, res
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    while i <= q: # 왼쪽 배열 부분이 남은 경우
        tmp.append(a[i])
        i += 1
    while j <= r: # 오른쪽 배열 부분이 남은 경우
        tmp.append(a[j])
        j += 1

    i = p
    t = 0

    while i <= r: # 결과를 a에 저장
        a[i] = tmp[t]
        cnt += 1
        if cnt == k:
            res = a[i]
            break
        i += 1
        t += 1

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
res = -1
merge_sort(a, 0, n - 1)
print(res)