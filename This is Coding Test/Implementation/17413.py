s = input()
arr = ''

if s.find('<'):
    s = list(s)
    s.reverse()
    s = ''.join(s)
    print(s)
else:
    for i in range(len(s)):
        idx = 0
        if s[i] == '<':
            # < 다음부터 확인해서 > 있으면 해당 인덱스 반환 및 break
            for j in range(i+1, len(s)):
                if s[j] == '>':
                    idx = j
                    break
            # <부터 > 에 해당하는 문자열 삽입
            arr += s[i:idx+1]
        # 닫혔으면 < 의 인덱스를 찾아서 반환
        if s[i] == '>':
            for j in range(i+1, len(s)):
                if s[j] == '<':
                    idx = j
                    break
            tmp =list(s[i+1:idx])
            tmp.reverse()
            tmp = ''.join(tmp)
            arr += tmp
        # 공백이면 
                
    print(arr)
#print(s[0:6])