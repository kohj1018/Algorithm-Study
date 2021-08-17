# T = int(input())
# for _ in range(T):
#     x, y = map(int, input().split())
#     distance = y - x
#     if distance == 4:
#         print(3)
#     else:
#         for i in range(1, distance):
#             temp_time = i**2 + i
#             if distance // temp_time == 1:
#                 if distance % temp_time == 0:
#                     print(2 * i)
#                 else:
#                     print(2 * i + 1)
#                 break
