N = int(input())
sizeList = []

for _ in range(N):
    x, y = map(int, input().split())
    sizeList.append((x, y))

for size in sizeList:
    rank = 1
    for compare_size in sizeList:
        if size[0] < compare_size[0] and size[1] < compare_size[1]:
            rank += 1
    print(rank, end=' ')
