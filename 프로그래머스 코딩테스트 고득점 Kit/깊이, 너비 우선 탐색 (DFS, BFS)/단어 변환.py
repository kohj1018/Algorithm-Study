from collections import deque


def solution(begin, target, words):
    answer = 0
    wordsNum = len(words)
    visited = [0 for _ in range(wordsNum)]

    queue = deque()
    queue.append(begin)
    while queue:
        popWord = queue.popleft()
        if popWord == target:
            answer = visited[words.index(target)]
            break
        for i in range(wordsNum):
            if visited[i] == 0:  # 아직 방문하지 않은 단어만 방문함
                check = 0
                for j in range(len(popWord)):
                    if popWord[j] != words[i][j]:
                        check += 1
                if check == 1:  # 단어 비교를 했을 때 한 알파벳만 다른 경우
                    if popWord == begin:  # 첫 단어에서 시작한 경우
                        visited[i] = 1
                    else:
                        visited[i] = visited[words.index(popWord)] + 1
                    queue.append(words[i])


    return answer