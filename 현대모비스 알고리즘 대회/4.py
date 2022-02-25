def solution(p, q):
    answer = []
    for idx in range(len(p)):
        cur_p = p[idx]
        cur_q = q[idx]
        if cur_p == cur_q:
            answer.append(True)
            continue
        for i in range(len(cur_p)-1):
            for j in range(i+1, len(cur_p)):
                

    return answer