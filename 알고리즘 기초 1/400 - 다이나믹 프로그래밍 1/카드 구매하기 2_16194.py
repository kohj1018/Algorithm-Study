N = int(input())
cost = [0]
cost += list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = cost[1]
dp[2] = min(cost[2], cost[1]*2)

for i in range(3, N+1):
    dp[i] = cost[i]
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[N])
