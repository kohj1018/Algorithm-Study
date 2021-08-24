# Stack 두 개를 이용한 풀이
import sys

N = int(sys.stdin.readline())

stack_1 = []    # deque 의 front
stack_2 = []    # deque 의 back
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push_front":
        stack_1.append(command[1])
    elif command[0] == "push_back":
        stack_2.append(command[1])
    elif command[0] == "pop_front":
        if stack_1:
            print(stack_1.pop())
        else:
            if stack_2:
                print(stack_2.pop(0))
            else:
                print(-1)
    elif command[0] == "pop_back":
        if stack_2:
            print(stack_2.pop())
        else:
            if stack_1:
                print(stack_1.pop(0))
            else:
                print(-1)
    elif command[0] == "size":
        print(len(stack_1) + len(stack_2))
    elif command[0] == "empty":
        if stack_1 or stack_2:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if stack_1:
            print(stack_1[-1])
        else:
            if stack_2:
                print(stack_2[0])
            else:
                print(-1)
    elif command[0] == "back":
        if stack_2:
            print(stack_2[-1])
        else:
            if stack_1:
                print(stack_1[0])
            else:
                print(-1)


# 파이썬 내장함수 deque을 이용한 풀이 ↓
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
#
# deq = deque()
# for _ in range(N):
#     command = sys.stdin.readline().rstrip().split()
#     if command[0] == "push_front":
#         deq.appendleft(command[1])
#     elif command[0] == "push_back":
#         deq.append(command[1])
#     elif command[0] == "pop_front":
#         if deq:
#             print(deq.popleft())
#         else:
#             print(-1)
#     elif command[0] == "pop_back":
#         if deq:
#             print(deq.pop())
#         else:
#             print(-1)
#     elif command[0] == "size":
#         print(len(deq))
#     elif command[0] == "empty":
#         if deq:
#             print(0)
#         else:
#             print(1)
#     elif command[0] == "front":
#         if deq:
#             print(deq[0])
#         else:
#             print(-1)
#     elif command[0] == "back":
#         if deq:
#             print(deq[-1])
#         else:
#             print(-1)
