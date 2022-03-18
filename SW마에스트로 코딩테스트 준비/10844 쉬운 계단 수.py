"""
1. 아이디어
그냥 bfs로 해서 풀면 될듯

2. 시간복잡도
- O(N^2)

3. 자료구조
N: int;
cnt: int;
"""
import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N]) % 1000000000)



# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N = int(input())
# cnt = 0
#
# queue = deque()
# for i in range(1, 10):
#     queue.clear()
#     queue.append([i, 1])
#     while queue:
#         popNum, length = queue.popleft()
#         if length == N:
#             cnt += 1
#         for newNum in (popNum-1, popNum+1):
#             if 0<=newNum<10 and length < N:
#                 queue.append([newNum, length+1])
#
# print(cnt % 1000000000)






# """
# 1. 아이디어
# 백트래킹으로 순회하며 갯수를 세면 된다.
# 0과 9를 제외한 나머지 수에서는 다음 수로 총 두 가지 경우의 수가 나올 수 있다.
# N+1짜리 배열을 만들고 수를 넣었다 뺐다하면서 총 개수를 구하면 된다.
#
# 2. 시간복잡도
#
# 3. 자료구조
# N: int;
# num: int[];
# cnt: int;
# """
# import sys
# sys.setrecursionlimit(10 ** 6)
#
# input = sys.stdin.readline
#
# N = int(input())
# cnt = 0
#
# def backTracking(depth):
#     if depth == N:
#         global cnt
#         cnt += 1
#         return
#     elif num[-1] == 0:
#         num.append(1)
#         backTracking(depth + 1)
#         num.pop()
#     elif num[-1] == 9:
#         num.append(8)
#         backTracking(depth + 1)
#         num.pop()
#     else:
#         for i in (num[-1] - 1, num[-1] + 1):
#             num.append(i)
#             backTracking(depth + 1)
#             num.pop()
#
#
# for i in range(1, 10):
#     num = [i]
#     backTracking(1)
#
# print(cnt % 1000000000)