maxNum = 0
idx = 0
for i in range(1, 10):
    num = int(input())
    if num > maxNum:
        maxNum = num
        idx = i

print(maxNum, idx, sep='\n')

# 더 짧은 코드 풀이 ↓
# arr = []
# for _ in range(9):
#     arr.append(int(input()))
#
# print(max(arr))
# print(arr.index(max(arr)) + 1)
