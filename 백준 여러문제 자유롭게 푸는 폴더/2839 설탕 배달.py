import sys

input = sys.stdin.readline

N = int(input())

def min_cnt(N):
    max_five_kilogram_cnt = N // 5
    for five_kilogram_cnt in range(max_five_kilogram_cnt, -1, -1):
        remain_kilogram = N - five_kilogram_cnt * 5
        if remain_kilogram % 3 == 0:
            return five_kilogram_cnt + remain_kilogram // 3
    return -1

print(min_cnt(N))