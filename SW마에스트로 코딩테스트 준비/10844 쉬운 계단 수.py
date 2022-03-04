"""
1. 아이디어
백트래킹으로 순회하며 갯수를 세면 된다.
0과 9를 제외한 나머지 수에서는 다음 수로 총 두 가지 경우의 수가 나올 수 있다.
N+1짜리 배열을 만들고 수를 넣었다 뺐다하면서 총 개수를 구하면 된다.

2. 시간복잡도

3. 자료구조
N: int;
num: int[];
cnt: int;
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())
cnt = 0

def backTracking(depth):
    if depth == N:
        global cnt
        cnt += 1
        return
    elif num[-1] == 0:
        num.append(1)
        backTracking(depth + 1)
        num.pop()
    elif num[-1] == 9:
        num.append(8)
        backTracking(depth + 1)
        num.pop()
    else:
        for i in (num[-1] - 1, num[-1] + 1):
            num.append(i)
            backTracking(depth + 1)
            num.pop()


for i in range(1, 10):
    num = [i]
    backTracking(1)

print(cnt % 1000000000)