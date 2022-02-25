import itertools

N, K = map(int, input().split())
words = []

for _ in range(N):
    words.append(input())

words = list(itertools.combinations(words, K))

fetch = False
for i in range(len(words)):
    origin = []
    new = []
    for j in range(K):
        origin.append(words[i][j][0])
        new.append(words[i][j][-1])
    new = list(itertools.permutations(new, K))
    for l in range(len(new)):
        if list(new[l]) == origin:
            fetch = True
            break
    if fetch: break

if fetch:
    print("YES")
else:
    print("NO")
