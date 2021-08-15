N = input()
if int(N) < 10:
    N = "0" + N

calNum = N[1] + str(int(N[0]) + int(N[1]))[-1]
count = 1

while calNum != N:
    calNum = calNum[1] + str(int(calNum[0]) + int(calNum[1]))[-1]
    count += 1

print(count)


# 배운 새로운 풀이↓
# N = int(input())
# new_N = N
# cnt = 0
#
# while True:
#     new_N = (new_N % 10) * 10 + (new_N // 10 + new_N % 10) % 10
#     cnt += 1
#     if new_N == N:
#         break
#
# print(cnt)
