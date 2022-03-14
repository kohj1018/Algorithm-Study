"""
1. 아이디어
a n t i c 5개
5개의 글자는 무조건 알아야 한다. 만약 K가 5미만이라면 0 출력
그리고 26글자를 다 가진 경우 모든 단어를 표현할 수 있으므로 N 출력
입력으로 받은 단어를 set함수를 이용해서 집합으로 형변환하여 중복을 없앰.

백트래킹으로 K-5개의 알파벳을 고름.
중복 없이 뽑는 조합이므로 재귀가 멈추는 if문은 뽑은 알파벳의 개수가 K-5개 일때고
뽑은 알파벳 순서 이후의 알파벳부터 for문을 돌려 다른 알파벳들을 뽑아나감.

2. 시간복잡도
- O(K^2)        -> 가능

3. 자료구조
N, K: int;
words: str{}[];
isLearn: bool[];
curCnt: int;
maxCnt: int;
"""
import sys
sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

N, K = map(int, input().split())
if K < 5:
    print(0)
elif K >= 26:
    print(N)
else:
    words = [set(input().rstrip()) for _ in range(N)]
    isLearn = [False] * 26
    for essentialChar in ('a', 'n', 't', 'i', 'c'):
        isLearn[ord(essentialChar) - ord('a')] = True

    maxCnt = 0


    def backTracking(idx, learnCharNum):
        if learnCharNum == K-5:
            global maxCnt
            curCnt = N
            for word in words:
                for char in word:
                    if not isLearn[ord(char) - ord('a')]:
                        curCnt -= 1
                        break
            if curCnt > maxCnt:
                maxCnt = curCnt
            return

        for i in range(idx+1, 26):
            if not isLearn[i]:
                isLearn[i] = True
                backTracking(i, learnCharNum + 1)
                isLearn[i] = False


    backTracking(0, 0)
    print(maxCnt)