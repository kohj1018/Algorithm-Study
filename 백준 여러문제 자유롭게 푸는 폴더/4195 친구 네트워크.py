import sys

input = sys.stdin.readline

test_case_cnt = int(input())

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent, size):
    root_a = find_parent(a, parent)
    root_b = find_parent(b, parent)

    # 이 문제에서는 누가 대장이냐는 중요하지 않고, 같은 팀이라는 사실만 중요하기 때문에 대장을 뽑는 일관된 규칙을 갖지 않아도 괜찮다.
    if root_a != root_b:
        parent[root_b] = root_a
        size[root_a] += size[root_b]

    return root_a

for _ in range(test_case_cnt):
    F = int(input())

    parent = {}
    size = {}

    for _ in range(F):
        A, B = input().split()

        if A not in parent:
            parent[A] = A
            size[A] = 1
        if B not in parent:
            parent[B] = B
            size[B] = 1

        root = union_parent(A, B, parent, size)

        print(size[root])
