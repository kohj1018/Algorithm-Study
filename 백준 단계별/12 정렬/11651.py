N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))

# key=lambda를 이용해서 정렬할 기준을 x[1] 그리고 x[0]으로 잡음
coordinates.sort(key=lambda x: (x[1], x[0]))

for co in coordinates:
    print(co[0], co[1])


# 또 다른 풀이↓
# (그냥 x와 y를 바꾸는 풀이)
# N = int(input())
# coordinates = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     coordinates.append([b, a])
#
# coordinates.sort()
#
# for co in coordinates:
#     print(co[1], co[0])
