N = int(input())
grade = list(map(int, input().split()))
maxSco = max(grade)

grade = [i/maxSco*100 for i in grade]

print(sum(grade)/len(grade))


# 이거 컴프리헨션 이용해서 잘 푼듯 ㅎㅎ 뿌듯 ㅎㅎ