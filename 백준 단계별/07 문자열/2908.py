def swap(num):
    swap_num = num[2] + num[1] + num[0]
    return swap_num

A, B = map(swap, input().split())

if int(A) > int(B):
    print(A)
else:
    print(B)


# 더 간결한 풀이 ↓
# A, B = map(lambda num: num[::-1], input().split())
#
# print(A) if A > B else print(B)