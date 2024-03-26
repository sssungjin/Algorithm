from collections import defaultdict

def solution(participant, completion):
    answer = ''
    int_dict = defaultdict(int)    
    for i in participant:
        int_dict[i] += 1
    for i in completion:
        int_dict[i] -= 1
    for i in int_dict:
        if int_dict[i] >= 1:
            return i
        #print(i)
    return answer