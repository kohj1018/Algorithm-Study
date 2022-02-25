N, M = map(int, input().split())

def dfs(s):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if i in s:
            continue
        dfs(s + [i])

dfs([])
