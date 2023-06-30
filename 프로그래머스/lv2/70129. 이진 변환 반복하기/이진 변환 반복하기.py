def solution(s):
    zero = 0
    i = 1
    while True:
        zero += s.count('0')
        s = s.replace('0', '')
        if s == '1':
            break
        s = format(len(s), 'b')
        i += 1

    answer = [i,zero]
    return answer