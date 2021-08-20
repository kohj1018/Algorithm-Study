N = int(input())

coList = list(map(int, input().split()))
# 중복 값 제거한 후 정렬
coList_sort = sorted(list(set(coList)))

# 시간 단축을 위해 딕셔너리 인덱싱을 사용
dic = {coList_sort[i]: i for i in range(len(coList_sort))}

for co in coList:
    print(dic[co], end=' ')
