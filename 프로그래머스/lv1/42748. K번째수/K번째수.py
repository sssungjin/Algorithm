def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        new = array[commands[n][0]-1:commands[n][1]]
        new.sort()
        answer.append(new[commands[n][2]-1])
    return answer