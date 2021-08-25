# Bottom-Up 방식
T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0, 1, 2, 4]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp[n])


# Top-Down 방식
# T = int(input())
#
# def multipleCnt(num):
#     if num <= 2: return num
#     if num == 3: return 4
#     if dp[num] != 0: return dp[num]     # Memorization 부분
#     dp[num] = multipleCnt(num-1) + multipleCnt(num-2) + multipleCnt(num-3)
#     return dp[num]
#
# for _ in range(T):
#     n = int(input())
#
#     dp = [0] * (10 + 1)
#     print(multipleCnt(n))
