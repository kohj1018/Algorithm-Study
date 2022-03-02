"""
1. 아이디어
재귀 호출로 인한 시간복잡도를 줄여줄 수 있는 DP를 이용해야한다.
3차원 배열로 memoization을 만들면 되지 않을까..?
20 * 20 * 20의 공간만 있으면 된다.

2. 시간복잡도
- O(n^3) : 20 * 20 * 20 = 8000      -> 가능

3. 자료구조
a, b, c: int;
dp: int[][][];
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))