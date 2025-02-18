# #!!!! 계수(카운팅)정렬 이해 필요!! (아직 이해 X)
#
# import sys
#
# n = int(sys.stdin.readline())
#
# arr = []
# for i in range(n):
#     num = int(sys.stdin.readline())
#     arr.append(num)
#
# count_dict = {}
#
# for num in arr:
#     if num in count_dict:
#         count_dict[num] += 1
#
#     else:
#         count_dict[num] = 1
#
# result = []
# for num in range(max(arr) + 1):
#     while num in count_dict and count_dict[num] != 0:
#         result.append(num)
#         count_dict[num] -= 1
#
# for i in range(len(result)):
#     print(result[i])
#

import sys

n = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
