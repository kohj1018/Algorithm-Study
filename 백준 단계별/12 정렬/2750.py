###                < Insertion Sort >
N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))

for i in range(1, N):
    cursor = result[i]
    j = i
    while j > 0 and result[j-1] > cursor:
        result[j] = result[j-1]
        j -= 1
    result[j] = cursor

for k in range(N):
    print(result[k])


###                < Selection Sort >
N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))

for i in range(N-1):
    minNumIdx = i
    for j in range(i+1, N):
        if result[minNumIdx] > result[j]:
            minNumIdx = j
    temp = result[i]
    result[i] = result[minNumIdx]
    result[minNumIdx] = temp

for k in range(N):
    print(result[k])


###                < Bubble Sort >
N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))

for i in range(N):  # i는 이번에 sort 될 자리이다.
    for j in range(N-1, i, -1):
        if result[j] < result[j-1]:
            temp = result[j]
            result[j] = result[j-1]
            result[j-1] = temp

for k in range(N):
    print(result[k])
