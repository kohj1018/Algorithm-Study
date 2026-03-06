import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, T = map(int, input().split())

F = [list(input().strip()) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def find_parent(r, c):
    if parent[r][c] != (r, c):
        parent[r][c] = find_parent(*parent[r][c])
    return parent[r][c]


def union_parent(r_a, c_a, r_b, c_b):
    r_a, c_a = find_parent(r_a, c_a)
    r_b, c_b = find_parent(r_b, c_b)

    if (r_a, c_a) != (r_b, c_b):
        if B[r_a][c_a] == B[r_b][c_b]:
            if r_a == r_b:
                if c_a <= c_b:
                    parent[r_b][c_b] = (r_a, c_a)
                else:
                    parent[r_a][c_a] = (r_b, c_b)
            elif r_a < r_b:
                parent[r_b][c_b] = (r_a, c_a)
            else:
                parent[r_a][c_a] = (r_b, c_b)
        elif B[r_a][c_a] > B[r_b][c_b]:
            parent[r_b][c_b] = (r_a, c_a)
        else:
            parent[r_a][c_a] = (r_b, c_b)


def find_next_position(i, j, remainder):
    if remainder == 0:
        return i - 1, j
    elif remainder == 1:
        return i + 1, j
    elif remainder == 2:
        return i, j - 1
    else:
        return i, j + 1


order = {'T': 0, 'C': 1, 'M': 2}


def get_ordered_string(chars):
    sorted_chars = sorted(set(chars), key=lambda x: order[x])
    return "".join(sorted_chars)

for _ in range(T):
    parent = [[(r, c) for c in range(N)] for r in range(N)]
    group_repre = {key: [] for key in ['single', 'double', 'triple']}

    # 1. 아침 시간
    B = [[cell + 1 for cell in row] for row in B]

    # 2. 점심 시간
    ## 2-1. 그룹 형성 및 대표자 선정
    for i in range(N):
        for j in range(N):
            for check_i, check_j in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                if 0 <= check_i < N and 0 <= check_j < N:
                    if F[i][j] == F[check_i][check_j]:
                        union_parent(i, j, check_i, check_j)
    ## 2-2. 대표자에게 신앙심 전달 및 대표자 모으기
    for i in range(N):
        for j in range(N):
            if parent[i][j] != (i, j):
                B[i][j] -= 1
                repre_i, repre_j = find_parent(i, j)
                B[repre_i][repre_j] += 1
            else:
                repre_food = F[i][j]
                if repre_food == 'T' or repre_food == 'C' or repre_food == 'M':
                    group_repre['single'].append((i, j))
                if repre_food == 'TC' or repre_food == 'TM' or repre_food == 'CM':
                    group_repre['double'].append((i, j))
                if repre_food == 'TCM':
                    group_repre['triple'].append((i, j))

    # 3. 저녁 시간
    ## 3-1. 그룹 내 정렬
    group_repre['single'] = sorted(group_repre['single'], key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    group_repre['double'] = sorted(group_repre['double'], key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    group_repre['triple'] = sorted(group_repre['triple'], key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))

    ## 3-2. 전파 시작
    for i, j in group_repre['single'] + group_repre['double'] + group_repre['triple']:

        # 방어 상태면 넘기기
        is_alive = False
        if (i, j) in group_repre['single']: is_alive = True
        if (i, j) in group_repre['double']: is_alive = True
        if (i, j) in group_repre['triple']: is_alive = True

        if not is_alive:
            continue

        remainder = B[i][j] % 4
        next_i, next_j = find_next_position(i, j, remainder)
        x = B[i][j] - 1
        B[i][j] = 1
        while 0 <= next_i < N and 0 <= next_j < N and x > 0:
            if F[i][j] == F[next_i][next_j]:
                next_i, next_j = find_next_position(next_i, next_j, remainder)
                continue

            y = B[next_i][next_j]

            if x > y:
                F[next_i][next_j] = F[i][j]
                B[next_i][next_j] += 1
                x -= (y + 1)
            else:
                F[next_i][next_j] = get_ordered_string(F[i][j] + F[next_i][next_j])
                B[next_i][next_j] += x
                x = 0

            # 전파당한 대표 학생 방어상태로 바꾸기 (전파 불능)
            for key in group_repre:
                if (next_i, next_j) in group_repre[key]:
                    group_repre[key].remove((next_i, next_j))
                    break

    ## 3-3. 각 음식별 신앙심 총합 출력
    total_B = {key: 0 for key in ['TCM', 'TC', 'TM', 'CM', 'M', 'C', 'T']}

    for i in range(N):
        for j in range(N):
            total_B[F[i][j]] += B[i][j]

    print(" ".join(str(total_B[key]) for key in ['TCM', 'TC', 'TM', 'CM', 'M', 'C', 'T']))
