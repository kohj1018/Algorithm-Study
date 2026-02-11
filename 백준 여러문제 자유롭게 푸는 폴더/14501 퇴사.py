import sys

input = sys.stdin.readline

N = int(input())

consulting_table = [[0, 0]]
for _ in range(N):
    T, P = map(int, input().split())
    consulting_table.append([T, P])

dp = [0] * (N + 2)

for i in range(N, 0, -1):
    if consulting_table[i][0] + i - 1 > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], consulting_table[i][1] + dp[i + consulting_table[i][0]])

print(dp[1])