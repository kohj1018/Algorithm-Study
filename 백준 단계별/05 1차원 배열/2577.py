A = int(input())
B = int(input())
C = int(input())

count = [0] * 10

calNum = str(A * B * C)

for i in calNum:
    count[int(i)] += 1

for ele in count:
    print(ele)


# 더 좋은 풀이 ↓
# a = int(input())
# b = int(input())
# c = int(input())
#
# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))