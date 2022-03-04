"""
1. 아이디어
DP로 풀면 될 것 같다.
dp[i] = (i번째 계단 점수) + max(dp[i-1], dp[i-2])

2. 시간복잡도
- O(n)

3. 자료구조
N: int;
score: int[];
dp: int[];
"""
import sys

input = sys.stdin.readline

N = int(input())
score = [0] * 300
for i in range(N):
    score[i] = int(input())

dp = [0] * 300
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[1] + score[2], score[0] + score[2])
for i in range(3, N):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

print(dp[N-1])