"""
1. 아이디어
- 백트래킹으로 전수를 조사한다.
    - for문을 돌릴 때 마지막으로 선택한 선수보다 높은 번호의 선수들을 대상으로 한다.
    - 전체를 대상으로 돌리는게 아니라 N/2만큼 돌린다. (대칭이므로)
    - 깊이가 N/2에 도달하면 선택한 팀 구성을 대상으로 각각 팀의 능력치를 구한다.
    - 비교하여 현재 갖고 있는 최소값보다 작으면 교체한다.

2. 시간 복잡도
- NCN/2 * (N ** 2) = (N! / ((N - N/2)! * (N/2)!)) * (N ** 2) ~= 70,000,000      -> 가능

3. 변수
- N : int
- S : int[][]
- 선택한 팀원 리스트 : int[]
- 능력치 차이 최소값 : int
"""
# import sys
# INF = sys.maxsize
#
# input = sys.stdin.readline
#
# N = int(input())
# S = [[]]
# for _ in range(N):
#     S.append([0] + list(map(int, input().split())))
#
# selected_team = []
# min_diff = INF
# def backtracking(num, last_player):
#     if num == N // 2:
#         unselected_team = []
#         for i in range(1, N + 1):
#             if i not in selected_team:
#                 unselected_team.append(i)
#         team1_power = 0
#         for player1 in selected_team:
#             for player2 in selected_team:
#                 if player1 != player2:
#                     team1_power += S[player1][player2]
#         team2_power = 0
#         for player1 in unselected_team:
#             for player2 in unselected_team:
#                 if player1 != player2:
#                     team2_power += S[player1][player2]
#         global min_diff
#         if min_diff > abs(team1_power - team2_power):
#             min_diff = abs(team1_power - team2_power)
#         return
#     else:
#         for selected_player in range(last_player + 1, N + 1):
#             selected_team.append(selected_player)
#             backtracking(num + 1, selected_player)
#             selected_team.pop()
#
# backtracking(0, 0)
#
# print(min_diff)

import sys
INF = sys.maxsize

input = sys.stdin.readline

N = int(input())
S = [[]]
for _ in range(N):
    S.append([0] + list(map(int, input().split())))

visit = [False] * (N + 1)
min_diff = INF

def backtracking(num, last_player):
    if num == N // 2:
        team1_power = 0
        team2_power = 0
        for player1 in range(1, N + 1):
            for player2 in range(1, N + 1):
                if player1 != player2:
                    if visit[player1] and visit[player2]:
                        team1_power += S[player1][player2]
                    elif not visit[player1] and not visit[player2]:
                        team2_power += S[player1][player2]
        global min_diff
        min_diff = min(min_diff, abs(team1_power - team2_power))
        return
    else:
        for selected_player in range(last_player + 1, N + 1):
            visit[selected_player] = True
            backtracking(num + 1, selected_player)
            visit[selected_player] = False

backtracking(0, 0)

print(min_diff)