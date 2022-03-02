"""
1. 아이디어
일단 시간제한이 빡빡하므로 재귀를 사용하되 memorization을 사용해서 DP로 문제를 풀어야한다.
피보나치 수열  : 0 1 1 2 3 5 8 13
0이 나온 횟수 : 1 0 1 1 2 3 5 8
1이 나온 횟수 : 0 1 1 2 3 5 8 13
위의 규칙을 보면 0은 0대로 1은 1대로 피보나치 수열 규칙으로 만들어진다.
따라서 memoization 수열 두 개 만들고 풀면 될 것이다. (잘하면 한 개로도 가능할지도..?)

2. 시간복잡도
- O(n)

3. 자료구조
T: int;
N: int;
dp: int[];
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # 0 1 2 3 4 5 6 7 8
    # 1 0 1 1 2 3 5 8 13
    dp = [0] * (N + 2)
    dp[0] = 1

    for i in range(2, N + 2):
        dp[i] = dp[i-1] + dp[i-2]

    print('{} {}'.format(dp[N], dp[N+1]))