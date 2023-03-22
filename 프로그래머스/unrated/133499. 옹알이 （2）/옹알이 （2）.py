def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    lst = []
    flag = 0
    for i in range(4):
        for j in range(len(babbling)):
            babbling[j] = babbling[j].replace(word[i], str(i))
    print(babbling)
    
    for i in range(len(babbling)):
        flag = 0
        if babbling[i].isdigit():
            for j in range(len(babbling[i])-1):
                if babbling[i][j] == babbling[i][j+1]:
                    flag = 1
            if flag == 0:
                answer += 1
    return answer

#연속X