"""
1. 아이디어
연산의 최솟값이므로 BFS로 탐색하면 된다.
for문으로 2를 곱하는 경우와 1을 수의 가장 오른쪽에 추가하는 경우를 둬서 확인한다.
bfs로 탐색하므로 처음 완성됐을 때가 필요한 연산의 최솟값이므로 그때 값을 출력하고 break하면 된다.

2. 시간복잡도
-

3. 자료구조
A, B: str;
"""
import sys
from collections import deque

input = sys.stdin.readline

A, B = input().split()


queue = deque()
queue.append([A, 1])
fetch = False
while queue:
    popA, num = queue.popleft()
    if popA == B:
        print(num)
        fetch = True
        break
    for newA in (popA + "1", str(int(popA) * 2)):
        if int(newA) <= int(B):
            queue.append([newA, num + 1])

if not fetch:
    print(-1)