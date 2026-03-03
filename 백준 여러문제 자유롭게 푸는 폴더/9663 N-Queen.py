# 비트 마스킹 풀이

import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

def bitmask(row, col, left, right):
    global cnt

    if row == N:
        cnt += 1
        return

    available = ((1 << N) - 1) &  ~(col | left | right)

    while available:
        p = available & -available

        bitmask(row + 1, col | p, (left | p) << 1, (right | p) >> 1)

        available -= p

bitmask(0, 0, 0, 0)
print(cnt)


# 백트래킹 풀이

# import sys
# sys.setrecursionlimit(10**6)
#
# input = sys.stdin.readline
#
# N = int(input())
#
# def isValid(x, y):
#     if not col_visited[y] and not left_diagonal_visited[x + y] and not right_diagonal_visited[x - y + N - 1]:
#         return True
#     else:
#         return False
#
# col_visited = [False] * N
# left_diagonal_visited = [False] * (2 * N - 1)
# right_diagonal_visited = [False] * (2 * N - 1)
#
# cnt = 0
#
# def backtracking(x):
#     global cnt
#
#     if x == N:
#         cnt += 1
#         return
#
#     for y in range(N):
#         if isValid(x, y):
#             col_visited[y] = True
#             left_diagonal_visited[x + y] = True
#             right_diagonal_visited[x - y + N - 1] = True
#             backtracking(x + 1)
#             col_visited[y] = False
#             left_diagonal_visited[x + y] = False
#             right_diagonal_visited[x - y + N - 1] = False
#
# backtracking(0)
# print(cnt)