N, M = map(int, input().split())

trust_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    trust_matrix[B][A] = 1

linked_computer_num = [0] * (N + 1)

def is_linked(original, v, is_visited):
    for next_v in trust_matrix[v]:
        if next_v == 1 and is_visited[next_v] != 1:
            linked_computer_num[original] += 1
            is_visited[next_v] = 1
            is_linked(original, next_v, is_visited)

for i in range(1, N + 1):
    is_visited = [0] * (N + 1)
    is_linked(i, i, is_visited)

top_1 = [0, 0]
for idx, value in enumerate(linked_computer_num):
    if value > top_1[1]:
        top_1[0] = idx
        top_1[1] = value

top_2 = [0, 0]
for idx, value in enumerate(linked_computer_num):
    if value > top_2[1] and idx != top_1[0]:
        top_2[0]= idx
        top_2[1] = value


result = sorted(map(int, (top_1[0], top_2[0])))

print(" ".join(map(str, result)))