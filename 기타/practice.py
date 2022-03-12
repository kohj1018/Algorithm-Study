import sys

input = sys.stdin.readline

N = int(input())
size = []
for _ in range(N):
    x, y = map(int, input().split())
    size.append([x, y])

for i in range(len(size)):
    rank = 1
    for j in range(len(size)):
        if size[j][0] > size[i][0] and size[j][1] > size[i][1]:
            rank += 1
    print(rank, end=' ')