"""
1. 아이디어
for문으로 1부터 N까지 돌리면서 이미 선택한 값이 아닌 경우 선택
M개 선택하는 경우 출력하고 return
하나의 리스트를 사용할 것이고 return해서 위 depth로 올라왔을 때 그대로 append만 하면
기존 리스트의 옆에 붙을테니 백트래킹 방식으로 return할 때 리스트 맨 끝을 지워주는 처리를 해줘야함.

2. 시간복잡도
- BackTracking
- 중복이 가능한 경우 : O(N^N)   (N = 8까지 가능)    (시간제한 1초인데 1초에 2억까지 처리가능하므로)
- 중복이 불가능한 경우 : O(N!)   (N = 10까지 가능)
- 중복이 불가능하면 depth가 깊어짐에 따라 N개에서 하나씩 줄어드니까 N!인 것

3. 자료구조
N, M: int;
result = int[];
visited = bool[];
"""
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 사용 시 필수! 재귀 깊이 제한 늘려서 런타임에러 없애기 용

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
visited = [False] * (N + 1)


def backTracking(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backTracking(num + 1)
            visited[i] = False
            result.pop()


backTracking(0)

# 다른 풀이 ↓
# def backTracking2(num):
#     if num == M:
#         print(' '.join(map(str, result)))
#         return
#     for i in range(1, N + 1):
#         if i not in result:     # in연산자를 사용하면 visited 리스트 없이도 구현가능
#             result.append(i)    # 하지만 O(n)만큼 더 순회하므로 시간복잡도 면에서는 visited를 사용하는게 좋다.
#             backTracking2(num + 1)
#             result.pop()