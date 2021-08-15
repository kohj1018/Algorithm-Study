N = int(input())

for _ in range(N):
    score = []
    TC = input()
    for i in range(len(TC)):
        if TC[i] == "O":
            if i != 0 and TC[i-1] == "O":
                score.append(score[i-1] + 1)
            else:
                score.append(1)
        else:
            score.append(0)
    print(sum(score))


# 더 간단한 방법 ↓
# N = int(input())
# 
# for _ in range(N):
#     TC = list(input())
#     sumSco = 0
#     pre_score = 0
#     for ele in TC:
#         if ele == "O":
#             sumSco += pre_score + 1
#             pre_score += 1
#         else:
#             pre_score = 0
#     print(sumSco)