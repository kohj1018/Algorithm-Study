N, M = map(int, input().split())


result = []

def backTracking(v):
    result.append(v)
    if len(result)-1 == M:
        print(' '.join(map(str, result[1:])))
        return
    for i in range(v+1, N+1):
        backTracking(i)
        result.pop()


backTracking(0)