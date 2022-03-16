def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: x[1])
    used = [False for _ in range(len(tickets))]

    def dfs(cityList, num):
        curCity = cityList[-1]
        if num == len(tickets):
            nonlocal answer
            answer = cityList
            return
        for i, ticket in enumerate(tickets):
            if not used[i] and ticket[0] == curCity:
                used[i] = True
                dfs(cityList + [ticket[1]], num+1)

    dfs(["ICN"], 0)

    return answer