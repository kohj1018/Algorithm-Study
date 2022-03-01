N = int(input())


def hanoi(num, from_, to, other):
    if num == 0: return     # base case
    hanoi(num-1, from_, other, to)
    print(from_, to)
    hanoi(num-1, other, to, from_)


print(2**N - 1)     # 하노이탑 최소 이동 횟수 출력
hanoi(N, 1, 3, 2)