# N = int(input())
#
# cnt = 0
# for _ in range(N):
#     cnt += 1
#     word = input()
#     check = ""
#     for i, letter in enumerate(word):
#         if i == 0:
#             check += letter
#         elif check.count(letter) > 0 and check[i-1] != letter:
#             cnt -= 1
#             break
#         else:
#             check += letter
#
# print(cnt)


# 또 다른 풀이 ↓
N = int(input())

# 카운트를 처음부터 전체 단어의 개수인 N으로 두어
# 그룹 단어가 아닐 경우 하나씩 빼는 방식으로 접근할 것이다.
cnt = N
for _ in range(N):
    word = input()
    for idx in range(len(word)-1):
        # idx를 기준으로 앞뒤 단어가 다를 경우
        if word[idx] != word[idx+1]:
            # idx 뒤쪽 인덱스의 문자열에서 word[idx+1] 문자가 포함되어 있는 지 확인
            if word[idx+1] in word[:idx]:
                # 포함되어 있다면 연속해서 알파벳이 나타난게 아니므로 cnt를 하나 감소 (그룹 단어가 아니다)
                cnt -= 1
                # 그리고 break로 for문 탈출(다음 단어로 넘어감)
                break
print(cnt)