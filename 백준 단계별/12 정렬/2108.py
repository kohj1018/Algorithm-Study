import sys
from collections import Counter

N = int(sys.stdin.readline())

numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline()))

print(round(sum(numList)/N))

numList.sort()
print(numList[N//2])

mode = Counter(numList).most_common(2)
if len(mode) > 1 and mode[0][1] == mode[1][1]:  # 최빈값이 두 개 이상
    print(mode[1][0])
else:
    print(mode[0][0])

print(max(numList)-min(numList))



# 최빈값에서 두번째 수를 구하는 방법에 더 좋은 방법이 있었다.↓
# collections 모듈의 Counter 클래스를 이용한다.
# from collections import Counter
#
# # most_common(2)로 빈도수가 높은 숫자 두 개를 가져온다.
# # (mode에는 튜플 형태로 값이 저장된다.)
# mode = Counter(numList).most_common(2)
# if len(mode) > 1:
#     if mode[0][1] == mode[1][1]:
#         print(mode[1][0])
#     else:
#         print(mode[0][0])
# else:
#     print(mode[0][0])
