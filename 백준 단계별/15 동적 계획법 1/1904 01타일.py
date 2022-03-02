"""
1. 아이디어
N :   1 2 3 4 5 6
개수 : 1 2 3 5 8 13
-> 점화식 : An = An-1 + An-2
점화식에 따라서 DP로 진행

2. 시간복잡도
- O(n)

3. 자료구조
N: int;
dp: int[];
"""
import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001      # 이거 (N+1)로 하면 런타임에러뜸..
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746     # 미리미리 나눠줘야한다. 마지막 출력에서 나누면 메모리 초과나옴.

print(dp[N])