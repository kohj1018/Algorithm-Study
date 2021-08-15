remainders = []

for _ in range(10):
    rem = int(input()) % 42
    if rem not in remainders:
        remainders.append(rem)

print(len(remainders))


# 집합 set을 이용한 풀이 ↓
# arr = []
# for i in range(10):
#     n = int(input())
#     arr.append(n % 42)
# arr = set(arr)
# print(len(arr))