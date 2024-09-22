n = int(input())

arr = []
for _ in range(n):
    tmp = list(input().split())
    arr.append(tmp)

tar = sorted(arr)
# for i in range(n - 1):
#     for j in range(i, n):
#         if tar[i][0] > tar[j][0]:
#             tar[i], tar[j] = tar[j], tar[i]

# 만약 나이가 같을 때 tar arr 순서 다르면 arr 대로 바꾸기

