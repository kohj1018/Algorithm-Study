N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))
coordinates.sort()
for co in coordinates:
    print("{} {}".format(co[0], co[1]))
