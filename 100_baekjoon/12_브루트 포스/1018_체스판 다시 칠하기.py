n, m = map(int, input().split())

arr = []
for i in range(n):
    row = input()
    arr.append(list(row))

print(arr[0])
tar = []
for i in range(n - 7):
    for j in range(m - 7):
        tar.append(arr[i][j])

print(tar)
# cnt = 0
# if arr[0][0] == 'W':
#     for i in range(n):
#         for j in range(m):
#             if i % 2 == 0 and j % 2 == 0:
#                 if arr[i][j] != 'W':
#                     cnt += 1
#
#             elif i % 2 == 1 and j % 2 == 1:
#                 if arr[i][j] != 'W':
#                     cnt += 1
#
#             elif i % 2 == 0 and j % 2 == 1:
#                 if arr[i][j] != 'B':
#                     cnt += 1
#
#             elif i % 2 == 1 and j % 2 == 0:
#                 if arr[i][j] != 'B':
#                     cnt += 1
#
# else:
#     for i in range(n):
#         for j in range(m):
#             if i % 2 == 0 and j % 2 == 0:
#                 if arr[i][j] != 'B':
#                     cnt += 1
#
#             elif i % 2 == 1 and j % 2 == 1:
#                 if arr[i][j] != 'B':
#                     cnt += 1
#
#             elif i % 2 == 0 and j % 2 == 1:
#                 if arr[i][j] != 'W':
#                     cnt += 1
#
#             elif i % 2 == 1 and j % 2 == 0:
#                 if arr[i][j] != 'W':
#                     cnt += 1
#
# print(cnt)

# Linux Master 1급 가자!!