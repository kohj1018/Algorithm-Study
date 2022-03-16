def solution(numbers, target):
    answer = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        for nextAns in (result+numbers[idx], result-numbers[idx]):
            dfs(idx+1, nextAns)

    dfs(0, 0)

    return answer