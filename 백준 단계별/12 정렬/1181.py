N = int(input())

words_list = []
for _ in range(N):
    word = input()
    words_list.append((word, len(word)))

# 중복 제거
words_list = list(set(words_list))

# 단어 길이 정렬 > 단어 알파벳 정렬
words_list.sort(key=lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])
