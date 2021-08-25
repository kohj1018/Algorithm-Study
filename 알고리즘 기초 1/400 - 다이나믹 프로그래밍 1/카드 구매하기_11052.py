N = int(input())
# 편의상 cost 리스트의 0번 인덱스는 사용 x
cost = [0]
cost += list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = cost[1]
dp[2] = max(cost[2], cost[1]*2)

for i in range(3, N+1):
    dp[i] = cost[i]     # i개 들어있는 카드팩을 하나 사는 경우
    for j in range(1, i//2 + 1):    # j와 i-j로 만드는 경우
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
