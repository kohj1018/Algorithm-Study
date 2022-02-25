# 35.6 / 80.0
def solution(a):
    answer = []
    for s in a:
        answer.append(dfs(s))
    return answer

def dfs(s):
    a_cnt = s.count("a")
    if a_cnt == 0: return False

    if s == "a": return True

    if a_cnt != 0 and s[0:a_cnt] == "b" * a_cnt and s[-a_cnt:len(s)] == "b" * a_cnt:
        if dfs(s[a_cnt:-a_cnt]): return True

    if s[0] == "a":
        if dfs(s[1:]): return True

    if s[-1] == "a":
        if dfs(s[:-1]): return True

    return False

# TC : abab bbaa bababa bbbabababbbaa
print(solution(input().split()))

# s = "abcdef"
# print(s[2:-2])   # ef

# s = "bbababb"
# print(s.split("a"))