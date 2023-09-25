from itertools import permutations

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
possible_numList = list(permutations(data, 3))

N = int(input())
for _ in range(N):
    given_numbers, strike, ball = map(int, input().split())
    given_numbers = list(str(given_numbers))

    remove_cnt = 0  # 중간의 리스트 길이를 변경하기 때문에 필요한 변수
    for i in range(len(possible_numList)):
        i -= remove_cnt
        possible_numbers = possible_numList[i]
        sCnt, bCnt = 0, 0
        for num in given_numbers:
            if num in possible_numbers: # 질문한 숫자 중 선택된 숫자 하나가 num의 possible_numbers안에 있는가
                if given_numbers.index(num) == possible_numbers.index(num): # 있고, 위치도 같으면 스트라이크 횟수 ++
                    sCnt += 1
                else:   # 위치는 다르지만 있다면 볼 횟수 ++
                    bCnt += 1
        if sCnt != strike or bCnt != ball:
            possible_numList.remove(possible_numbers)
            remove_cnt += 1

print(len(possible_numList))