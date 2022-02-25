def solution(dice):
    for i in range(1, 1000000):
        check_dice = list(dice)
        for numPart in str(i):
            for idx, current_dice in enumerate(check_dice):
                if int(numPart) in current_dice:
                    check_dice.pop(idx)
                    break
        # 수를 만들지 못한 경우
        if len(str(i)) != len(dice) - len(check_dice):
            answer = i
            return answer

print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))



# def dfs(s):
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, N+1):
#         if i in s:
#             continue
#         dfs(s + [i])
