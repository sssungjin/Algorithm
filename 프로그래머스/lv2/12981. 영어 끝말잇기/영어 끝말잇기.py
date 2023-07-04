def solution(n, words):
    answer = []
    
    for i in range(1,len(words)):
        if words[i] in words[:i]:
            answer = [i%n+1,i//n+1]
            break
        elif i < len(words)-1:
            if words[i][0] != words[i-1][-1]:
                answer = [i%n+1,i//n+1]
                break
    if answer == []:
        return [0,0]
    return answer