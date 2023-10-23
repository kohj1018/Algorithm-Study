"""
1. 아이디어
- for 문 세개를 이용해 모든 경우를 조사한다.

2. 시간 복잡도
- O(N^3) : 100 ** 3 = 1,000,000     -> 가능

3. 변수
- N, M : int
- 가장 큰 합 : int
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))

max_sum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total_sum = li[i] + li[j] + li[k]
            if max_sum < total_sum <= M:
                max_sum = total_sum

print(max_sum)
