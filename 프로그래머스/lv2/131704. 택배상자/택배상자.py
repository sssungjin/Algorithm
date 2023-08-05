def solution(order):
    answer = 0
    sub = []
    for i in range(1,len(order)+1):
        #일단 보조에 넣고 확인
        sub.append(i)
        #sub에 마지막으로 넣은거랑 order가 같으면 pop하고 answer +1
        while sub and order[answer] == sub[-1]: #answer +1 헤서 인덱스로 사용
            sub.pop()
            answer += 1
    return answer

#main 올바른 순서, sub 보조, coming 오고 있는거, order 4개 pop,push 하면서 썼다가 시간초과 나서....