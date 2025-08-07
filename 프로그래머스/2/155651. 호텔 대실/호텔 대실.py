def solution(book_time):
    answer = 0
    book_time.sort()
    
    # time[:2], time[3:]
    # 시작시간: print(book_time[i][0][:2] + book_time[i][0][3:])
    # 퇴실시간: print(book_time[i][1][:2] + book_time[i][1][3:])
    rooms = [] # 끝나는 시간 넣기, 시작시간과 비교해서 끝 시간이 더 빠르다면 넣기
    # 퇴실 시키는 방법은 
    # print(int(book_time[0][0][:2]) * 60 + int(book_time[0][0][3:]), int(book_time[0][1][:2]) * 60 + int(book_time[0][1][3:]) + 10)
    # print(book_time)
    for time in book_time:
        start = int(time[0][:2]) * 60 + int(time[0][3:])
        end = int(time[1][:2]) * 60 + int(time[1][3:]) + 10 # (시간 + 분 + 청소)
        
        # 비어있으면 넣기
        if len(rooms) == 0:
            rooms.append(end)
        # 차있을때는 rooms의 end(작은것부터 비교시작)와 시작시간을 비교해서 start가 더 크다면 그 자리에 넣고 없다면 새로 넣기
        else:
            rooms.sort()
            for i in range(len(rooms)):
                if start >= rooms[i]:
                    del rooms[i]
                    rooms.append(end)
                    break
            else:
                rooms.append(end)
                
    return len(rooms)
                    
                
                    
            
        
        
    
    rooms = []
    
    
    return answer