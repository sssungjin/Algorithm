import math

def solution(fees, records):
    answer = []
    parking = {}
    total_time = {}
    
    for record in records:
        tmp, number, inout = record.split()
        hour, minute = map(int, tmp.split(":"))
        time = hour * 60 + minute
        
        if inout == "IN":
            #in이면 주차하는데 번호화 시간 기록
            parking[number] = time
        elif inout == "OUT":
            #out이면 나간 시간에서 주차한 시간을 빼서 총 주차 시간 기록
            if number in total_time:
                total_time[number] += (time - parking[number])
            else:
                total_time[number] = time - parking[number]
            #나갔으니까 주차에서 지워줌
            del parking[number]
            
    #안지워진 경우 -> out이 없는 경우는 23:59에 나간것으로 취급
    for number, time in parking.items():
        #한번 입출차 해서 시간 기록이 남아있는 경우
        if number in total_time:
            total_time[number] += 1439 - time
        else:
            total_time[number] = 1439 - time
    
    for number, time in sorted(total_time.items(), key=lambda x: x[0]):
        charge = fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3]
        answer.append(charge)
    
    return answer
