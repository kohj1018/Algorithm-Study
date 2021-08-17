coordinates = []
for _ in range(3):
    coordinates.append(list(map(int, input().split())))

result = [0, 0]
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        if coordinates[i][0] == coordinates[j][0]:
            result[0] = coordinates[3-(i+j)][0]
        elif coordinates[i][1] == coordinates[j][1]:
            result[1] = coordinates[3-(i+j)][1]
print(result[0], result[1], sep=' ')


# count를 이용한 더 좋은 풀이 (x좌표와 y좌표를 따로 받는 풀이)
# x_co = []
# y_co = []
# for _ in range(3):
#     x, y = map(int, input().split())
#     x_co.append(x)
#     y_co.append(y)
#
# for i in range(3):
#     if x_co.count(x_co[i]) == 1:
#         x = x_co[i]
#     if y_co.count(y_co[i]) == 1:
#         y = y_co[i]
# print(x, y)
