scores = []
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    scores.append(score)
print(int(sum(scores)/5))
