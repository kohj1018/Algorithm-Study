# stack 두 개를 이용해 시간 단축
# append, pop은 O(1)이다.
import sys

stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []
N = len(stack_1)
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "L" and stack_1:
        stack_2.append(stack_1.pop())
    elif command[0] == "D" and stack_2:
        stack_1.append(stack_2.pop())
    elif command[0] == "B" and stack_1:
        stack_1.pop()
    elif command[0] == "P":
        stack_1.append(command[1])

print("".join(stack_1 + list(reversed(stack_2))))


# 시간 초과가 난 최초의 내 코드 ↓
# string = list(input())
# N = len(string)
# M = int(input())
# cursor = N
#
# for _ in range(M):
#     command = input().split()
#     if command[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif command[0] == "D":
#         if cursor < N+1:
#             cursor += 1
#     elif command[0] == "B":
#         if cursor > 0:
#             string.pop(cursor-1)
#             cursor -= 1
#     elif command[0] == "P":
#         string.insert(cursor, command[1])
#         cursor += 1
#
# for s in string:
#     print(s, end='')
