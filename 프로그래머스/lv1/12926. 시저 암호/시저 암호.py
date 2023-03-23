def solution(s, n):
    answer = ''
    
    for i in s:
        #대문자 65~90
        #소문자 97~122
        if i.isupper():
            answer += chr((ord(i) - ord('A') + n)%26+ord('A'))
        elif i.islower():
            answer += chr((ord(i) - ord('a') + n)%26+ord('a'))
        else:
            answer += ' '

    return answer