"""
1. 아이디어
"-" 연산자를 기준으로 리스트를 나누고 각각의 리스트를 또 "+" 연산자를 기준으로 나누고 합함
그리고 각 리스트의 합들을 빼주기

2. 시간복잡도
- O(n^2)

3. 자료구조

"""
import sys

input = sys.stdin.readline

formula = input().rstrip().split("-")

for idx, numStr in enumerate(formula):
    formula[idx] = sum(map(int, numStr.split("+")))

result = formula[0]
for num in formula[1:]:
    result -= num

print(result)