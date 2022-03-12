"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1 2 2 3 3 3 4 4 4 4  5  5  5  5  5
"""
# numList = [0] * 1001
# numList[1] = 1
# for num in range(1, 51):
#     if (num * (num-1)) // 2 + 1 > 1000:
#         break
#     for i in range((num * (num-1)) // 2 + 1, (num * (num+1)) // 2 + 1):
#         if i > 1000:
#             break
#         numList[i] = num
#
# A, B = map(int, input().split())
# print(sum(numList[A:B+1]))

A, B = map(int, input().split())
arr = [0]
for num in range(46):
    for _ in range(num):
        arr.append(num)

print(sum(arr[A:B+1]))
