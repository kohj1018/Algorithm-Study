"""
1. 아이디어
그리디하게 1부터 선택해나가면 된다.
선택한 서로다른 자연수 중 가장 큰 자연수를 K라고 할 때,
1부터 K까지의 합은 (1+K)*K/2 이므로 이 값이 S를 초과하기 전까지의 K값을 구하면
K+1이 답이다.

2. 시간복잡도
- O(S)

3. 자료구조
S: int;
K: int;
"""
import sys

input = sys.stdin.readline

S = int(input())

k = 1
while k*(k+1)//2 <= S:
    k += 1
print(k-1)