T = int(input())

for _ in range(T):
    sentence = input().split()
    new_sentence = []
    for word in sentence:
        rev_word = ""
        for char in word:
            rev_word = char + rev_word
        new_sentence.append(rev_word)
    for word in new_sentence:
        print(word, end=' ')


# 더 괜찮은 풀이 ↓
# T = int(input())
#
# for _ in range(T):
#     sentence = input() + " "
#     stack = []
#     for char in sentence:
#         # 공백이 아니라면 스택에 문자 추가
#         if char != " ":
#             stack.append(char)
#         else:
#             # stack이 빌 때까지 while문이 돈다.
#             while stack:
#                 print(stack.pop(), end='')
#             print(' ', end='')
