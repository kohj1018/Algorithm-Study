# 기존의 알고리즘보다 더 효율적인 알고리즘
# (튜플을 이용해 [0]에는 현재 값을 넣고 [1]에는 이전 값을 넣는다.)
def fibonacci(num):
    if num < 2:
       return num, 0
    else:
        i, j = fibonacci(num-1)
        return i+j, i

print(fibonacci(int(input()))[0])
