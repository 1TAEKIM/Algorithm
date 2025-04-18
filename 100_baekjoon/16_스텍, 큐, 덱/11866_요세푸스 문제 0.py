n, k = map(int, input().split())

queue = [i for i in range(1, n + 1)]

idx = 0
res = []
while queue:
    idx += k - 1    # k-1번째 인덱스까지 건너뛰기
    if idx >= len(queue):   # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)   # 나머지 연산을 통해 인덱스 계산
    res.append(str(queue.pop(idx)))

# .join은 str형이 필요
print("<", ", ".join(res), ">", sep="")

