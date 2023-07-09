def solution(elements):
    tmp = []
    length = len(elements)
    elements = elements + elements
    for i in range(1,length+1):
        #i는 합을 구할 길이 1,2,3,4,5
        for j in range(length):
            #j는 시작위치 j ~ j+i 만큼의 합
            tmp.append(sum(elements[j:j+i]))
    return len(list(set(tmp)))