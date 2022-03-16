def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i] == 1:
                visited[i] = True
                dfs(i)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer