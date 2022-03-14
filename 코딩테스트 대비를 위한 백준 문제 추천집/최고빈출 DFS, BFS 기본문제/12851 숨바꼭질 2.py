"""
1. 아이디어
<백트래킹 접근>
가장 빠른 시간을 출력하고 '방법의 가짓수'도 출력해야하므로 dfs로 탐색해야한다.
최대 수는 동생 위치에서 수빈이의 위치를 뺀 값이고 해당 값에 도달하면 탐색을 마쳐야한다.
(그때까지 찾아도 못찾았다는건 최단거리 탐색에 실패한 트리가지인거니까)
dfs로 탐색했을 때 동생이 있는 점 K에 도달할 때 도달하는데 걸린 횟수를 저장한다.
그리고 다음에 또 도달하면 둘을 비교해 더 큰 값을 저장한다.
만약 같다면 같은 도달 시간 횟수를 체크한다.

<bfs풀이 접근>
bfs로 탐색한다.
visited 배열에 걸린 시간을 체크해서 적어두는데 이미 시간이 적힌 배열칸에 다시 접근하기 위해서
or 연산자를 이용해 visited[nextX] == visited[popX] + 1 를 추가한다.

2. 시간복잡도
-

3. 자료구조
N, K: int;
curShortestTime: int;
shortestPathCnt: int;
"""
import sys
from collections import deque
# sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
curShortestTime = 100000
shortestPathCnt = 0

queue = deque()
queue.append([N, 0])
visited[N] = 1
while queue:
    popX, timeTaken = queue.popleft()
    if timeTaken > curShortestTime:
        break
    if popX == K:
        if timeTaken == curShortestTime:
            shortestPathCnt += 1
        if timeTaken < curShortestTime:
            curShortestTime = timeTaken
            shortestPathCnt = 1
    for nextX in (popX-1, popX+1, 2*popX):
        if 0<=nextX<=100000:
            if visited[nextX] == 0 or visited[nextX] == visited[popX] + 1:
                visited[nextX] = visited[popX] + 1
                queue.append([nextX, timeTaken + 1])


print(curShortestTime)
print(shortestPathCnt)


# def dfs(x, timeTaken):
#     visited[x] = True
#     global curShortestTime
#     global shortestPathCnt
#     if timeTaken >= K - N:
#         if x == K and timeTaken < curShortestTime:
#             curShortestTime = timeTaken
#             shortestPathCnt = 1
#         return
#     if x == K:
#         if timeTaken < curShortestTime:
#             curShortestTime = timeTaken
#             shortestPathCnt = 1
#         elif timeTaken == curShortestTime:
#             shortestPathCnt += 1
#         return
#     for nextX in (x-1, x+1, 2*x):
#         if 0<=nextX<=100000 and not visited[nextX]:
#             visited[nextX] = True
#             dfs(nextX, timeTaken+1)
#             visited[nextX] = False
#
#
# dfs(N, 0)
# print(curShortestTime)
# print(shortestPathCnt)