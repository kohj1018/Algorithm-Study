# 두개의 인덱스를 받아 값을 바꾸는 함수
def swap(idx1, idx2):
    global result
    temp = result[idx1]
    result[idx1] = result[idx2]
    result[idx2] = temp

###                < Heap Sort >

N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))

# phaseⅠ : 가상의 max heap을 만드는 단계
for i in range(1, N):
    while i != 0:
        if i % 2 == 0:  # i가 짝수
            if result[(i-2)//2] < result[i]:
                swap(i, (i-2)//2)
                i = (i-2)//2
            else:
                break
        else:
            if result[(i-1)//2] < result[i]:
                swap(i, (i-1)//2)
                i = (i-1)//2
            else:
                break


# phaseⅡ : max heap에서 최대값을 하나씩 제거하며 sorting을 시행하는 단계
for i in range(N-1, 0, -1):
    swap(0, i)
    downHeapIdx = 0
    while 2 * downHeapIdx + 2 < i or i == 2:
        right_idx = 2 * downHeapIdx + 2
        left_idx = 2 * downHeapIdx + 1
        if i == 2:
            if result[downHeapIdx] < result[left_idx]:
                swap(0, 1)
            break
        if result[downHeapIdx] < result[left_idx] and result[left_idx] > result[right_idx]:
            swap(downHeapIdx, left_idx)
            downHeapIdx = left_idx
        elif result[downHeapIdx] < result[right_idx] and result[right_idx] > result[left_idx]:
            swap(downHeapIdx, right_idx)
            downHeapIdx = right_idx
        else:
            break

for k in range(N):
    print(result[k])


###                < Merge Sort >



###                < Quick Sort >