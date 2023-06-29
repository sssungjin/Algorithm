def solution(s):
    answer = ''
    slist = s.split()
    ilist = []
    for i in slist:
        ilist.append(int(i))
    answer = str(min(ilist)) + ' ' + str(max(ilist))
    return answer