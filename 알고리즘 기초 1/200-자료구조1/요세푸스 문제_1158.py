# N, K = map(int, input().split())
#
# circular_queue = [i for i in range(1, N+1)]
# cursor = K-1
# result = []
# while circular_queue:
#     result.append(str(circular_queue.pop(cursor)))
#     # 순서 중요! N 감소가 cursor 이동보다 선행되어야 함.
#     N -= 1
#     if N > 0:
#         if (cursor + K) % N == 0:
#             cursor = N - 1
#         else:
#             cursor = (cursor + K) % N - 1
#
# print("<" + ", ".join(result) + ">")


# 더 간결한 풀이 ↓
N, K = map(int, input().split())

circular_queue = [i for i in range(1, N+1)]
cursor = 0
result = []
for _ in range(N):
    # 제거하면 인덱스가 앞으로 밀린다. 때문에 -1 해주기
    cursor += K-1
    # 한바퀴 돌고 다시 인덱스 0으로 오는 경우 고려
    cursor %= len(circular_queue)
    result.append(str(circular_queue.pop(cursor)))

print("<" + ", ".join(result) + ">")
