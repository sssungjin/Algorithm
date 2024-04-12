# 배열에 나갔는지 들어왔는지와 함께 uid를 같이 저장, 변경하면 해당 uid의 닉네임 다 변경
# dict에 uid와 닉네임 record 순서대로 저장
# 그리고 해당 uid에 해당하는 닉네임으로 enter와 leave를 answer에 저장

def solution(record):
    answer = []
    dic = {}
    for rec in record:
        tmp = rec.split()
        if not tmp[0] == "Leave":
            # Leave가 아닐때 -> Enter거나 Change일때 이름을 최신화
            dic[tmp[1]] = tmp[2]
    
    # dic에 저장된 uid에 해당하는 이름으로 결과에 저장
    for rec in record:
        tmp = rec.split()
        if tmp[0] == "Enter":
            answer.append(dic[tmp[1]] + "님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            answer.append(dic[tmp[1]] + "님이 나갔습니다.")
        
    return answer