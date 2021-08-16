X = int(input())

line = 1
# 몇 번째 대각선 줄인지 구하기
while X > line:
    X -= line
    line += 1

# 짝수번째 대각선줄은 분자는 오름차순, 분모는 내림차순
if line % 2 == 0:
    a = X
    b = line - X + 1
# 홀수번째 대각선줄은 분자는 내림차순, 분모는 오름차순
else:
    a = line - X + 1
    b = X

print("{}/{}".format(a, b))
