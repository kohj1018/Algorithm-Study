"""
1. 아이디어
점화식 : An = An-2 + An-3
점화식 바탕으로 DP로 풀이

2. 시간복잡도
- O(n)

3. 자료구조
T: int;
N: int;
dp: int[];
"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N])
