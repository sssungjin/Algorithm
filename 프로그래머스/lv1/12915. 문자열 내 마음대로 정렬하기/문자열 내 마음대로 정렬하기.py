def solution(strings, n):
    answer = []
    a = []
    strings.sort()
    for i in range(len(strings)):
        tmp = (strings[i][n], strings[i])
        a.append(tmp)
    
    a.sort(key = lambda x:x[0])
    for i in a:
        answer.append(i[1])
    return answer