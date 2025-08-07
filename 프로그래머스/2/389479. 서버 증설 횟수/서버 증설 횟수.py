def solution(players, m, k):
    server_info = [] #[0]는 증설된 시간, [1]은 증설된 횟수
    total_cnt = 0 # 정답 (전체 증설 수)
    now_server = 0 # 현재 증설된 서버 수
    
    for time in range(24):
        # 
        ended_cnt = sum(cnt for (end_time, cnt) in server_info if end_time == time)
        now_server -= ended_cnt
        server_info = [(end_time, cnt) for (end_time, cnt) in server_info if end_time != time]
                
        # 필요한 서버 수
        n = players[time] // m
        # 증설 횟수
        if now_server < n:
            x = n - now_server
            server_info.append((time + k, x))
            total_cnt += x
            now_server += x
                
    return total_cnt
