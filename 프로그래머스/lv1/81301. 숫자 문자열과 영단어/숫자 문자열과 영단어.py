def solution(s):
    answer = 0
    en_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0,10):
        while en_number[i] in s:
            s = s.replace(en_number[i], str(i))
            
    answer = int(s)
    return answer