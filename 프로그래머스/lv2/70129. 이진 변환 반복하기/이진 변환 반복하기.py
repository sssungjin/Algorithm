def solution(s):
    zero = 0
    i = 0
    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        i += 1

    answer = [i,zero]
    return answer