# w + c 가 사전에 있는지 확인하고 있으면 글자 확장 없으면 w 번호 출력, w + c 사전 등록

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solution(msg):
    answer = []
    dic = {chr(i + 64): i for i in range(1, 27)}
    next_index = 27

    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1
        # 없으면 break 되고 w+c가 삽입됨
        while j <= len(msg) and msg[i:j] in dic:
            w = msg[i:j]
            j += 1
    
        answer.append(dic[w])

        if j <= len(msg):
            dic[msg[i:j]] = next_index
            next_index += 1

        i += len(w)
        
    return answer