"""
1. 아이디어
while문으로 숫자를 증가시켜가며 6이 연속으로 세번나오는걸 체크해 미리 만든 변수에 플러스 1한다.
그러다 N번째가 되면 출력.

2. 시간복잡도
- O(n)

3. 자료구조
N: int;
cnt: int;
currentN: int;
"""
N = int(input())

cnt = 1
num = 666
while N > cnt:
    num += 1
    if "666" in str(num):
        cnt += 1

print(num)
