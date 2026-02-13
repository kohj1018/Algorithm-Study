import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lan_cables = []
for _ in range(K):
    lan_cables.append(int(input()))

max_length = max(lan_cables)

def binary_search(start, end):
    max_cut_length = 0

    while start <= end:
        mid = (start + end) // 2

        cable_cnt = 0
        for cable in lan_cables:
            cable_cnt += cable // mid

        if cable_cnt >= N:
            start = mid + 1
            max_cut_length = mid
        else:
            end = mid - 1

    return max_cut_length

print(binary_search(1, max_length))