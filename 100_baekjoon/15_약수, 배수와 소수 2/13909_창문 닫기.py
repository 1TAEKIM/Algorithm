print(int(int(input()) ** 0.5))

"""
조건 범위가 클 때, 일부 값을 구해서
규칙성 파악해보기!!!!!!
"""

# n = int(input())
# # 각 창문 번호의 약수의 개수가 짝수 0, 홀수 1
# arr = []
# for n in range(1, 25):
#     ans = 0
#     for i in range(1, n + 1):
#         cnt = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 cnt += 1
#         if cnt % 2 == 0:
#             arr.append(0)
#         else:
#             arr.append(1)
#             ans += 1
#     print(ans)
