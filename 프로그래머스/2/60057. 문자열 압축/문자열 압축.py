def solution(s):
    result = []
    for i in range(1, len(s) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s) + i, i):
            # 같다면 cnt + 1
            if tmp == s[j:j + i]:
                cnt += 1
            # 다르다면 그 앞까지 계산한 cnt와 같았던 문자열 붙여주고 
            # tmp를 다음 문자열로 선언, cnt 1로 초기화
            else:
                # 1이 아니라면 중복 있었으니까 str(cnt)
                if cnt != 1:
                    b = b + str(cnt) + tmp
                # 1인 경우는 cnt 붙일 필요 없음
                else:
                    b = b + tmp
                    
                tmp = s[j:j+i]
                cnt = 1
        result.append(len(b))
    return min(result)