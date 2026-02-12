import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree_length = list(map(int, input().split()))
max_length = max(tree_length)

def binary_search(start, end):
    max_cut_height = 0

    while start <= end:
        mid = (start + end) // 2

        tree_sum = 0
        for h in tree_length:
            if h > mid:
                tree_sum += h - mid
        if tree_sum >= M:
            start = mid + 1
            if mid > max_cut_height:
                max_cut_height = mid
        else:
            end = mid - 1

    return max_cut_height

print(binary_search(0, max_length))




# 시간초과

# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# tree_length = list(map(int, input().split()))
# max_length = max(tree_length)
#
# def max_cut():
#     dp = [0] * (max_length + 2)
#     for current_cut in range(max_length, -1, -1):
#         tree_sum = 0
#         for h in tree_length:
#             if h > current_cut and h != 0:
#                 tree_sum += 1
#         dp[current_cut] = dp[current_cut + 1] + tree_sum
#
#         if dp[current_cut] >= M:
#             return current_cut
#
# print(max_cut())