def solution(elements):
    answer = 0
    length = len(elements)
    print(length)
    elements = elements + elements
    print(elements)
    tmp = []
    for i in range(1,length+1):
        #i는 길이 1,2,3,4,5
        for j in range(length):
            #j는 시작위치 0,1,2,3,4 j ~ j+i
            tmp.append(sum(elements[j:j+i]))
    answer = list(set(tmp))
    return len(answer)

#7911479114