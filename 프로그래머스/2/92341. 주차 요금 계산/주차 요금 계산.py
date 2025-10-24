from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    result = []
    # ceil 함수 활용
    
    # 주차 시간을 모두 구함
    # 기본 시간보다 적다면 기본 요금만
    # 기본 시간 넘어갔다면
    # 주차요금 = 기본 요금 + ceil((전체 시간 - 기본 시간) / 단위 시간) * 단위 요금
    # IN 이면 음수로 저장 -334 + 479, 그리고 IN이면 flag 값도 같이 저장
    # dic[key] = [시간, flag] flag가 True이면 23:59 출차 처리, 즉 + 60 * 23 + 59 해줘야함
    #
    
    last_out = 23 * 60 + 59
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    dic = defaultdict(list)
    
    for record in records:
        time, number, inout = record.split()
        hour, minute = map(int, time.split(':'))
        
        if not dic[number]:
            dic[number] = [0, False]
        
        if inout == 'IN':
            dic[number][0] -= hour * 60 + minute
            dic[number][1] = True
        else:
            dic[number][0] += hour * 60 + minute
            dic[number][1] = False
    
    for key, val in dic.items():
        if dic[key][1] == True:
            dic[key][0] += last_out
        
        if dic[key][0] <= default_time:
            result.append([key, default_fee])
        else:
            fee = default_fee + math.ceil((dic[key][0] - default_time) / unit_time) * unit_fee
            result.append([key, fee])
    
    result.sort()
    
    for r in result:
        answer.append(r[1])
    
    return answer