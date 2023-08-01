def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-sum(number)+1):
        s = discount[i:sum(number)+i]
        cnt = 0
        for w,n in zip(want, number):
            if s.count(w) >= n:
                continue
            else:
                cnt += 1
        if cnt == 0: answer += 1
    return answer

