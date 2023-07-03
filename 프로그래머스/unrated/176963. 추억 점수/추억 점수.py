def solution(name, yearning, photo):
    answer = []
    for i in photo:
        tmp = 0
        for j in i:
            if j in name:
                tmp += yearning[name.index(j)]
        answer.append(tmp)
    return answer