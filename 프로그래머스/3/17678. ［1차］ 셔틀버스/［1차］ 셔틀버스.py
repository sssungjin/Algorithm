def solution(n, t, m, timetable):
    int_timetable = []
    for time in timetable:
        hh = int(time[:2])
        mm = int(time[3:])
        int_timetable.append(hh * 60 + mm)
    int_timetable.sort()

    current_bus_time = 9 * 60
    
    crew_idx = 0
    
    last_bus_passengers = [] 

    for i in range(n):
        
        # 현재 버스에 탈 수 있는 크루들을 태움
        passengers_on_this_bus = []
        while crew_idx < len(int_timetable) and len(passengers_on_this_bus) < m:
            crew_arrival_time = int_timetable[crew_idx]
            
            if crew_arrival_time <= current_bus_time:
                passengers_on_this_bus.append(crew_arrival_time)
                crew_idx += 1
            else:
                break # 다음 크루는 현재 버스 시간보다 늦게 오므로 태울 수 없음

        # 현재 버스가 마지막 버스라면 탑승객 정보를 저장
        if i == n - 1:
            last_bus_passengers = passengers_on_this_bus
            
        current_bus_time += t

    answer_min = 0
    if len(last_bus_passengers) < m:
        # 자리가 남았으므로, 마지막 버스 도착 시간에 맞춰오면 됨
        answer_min = current_bus_time - t
    else:
        # 꽉 찼으므로, 마지막 탑승객보다 1분 일찍 와야 함
        answer_min = last_bus_passengers[-1] - 1

    h = answer_min // 60
    minute = answer_min % 60
    return f"{h:02d}:{minute:02d}"