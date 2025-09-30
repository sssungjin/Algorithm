from collections import deque

def solution(players, m, k):
    answer = 0
    
    n = 0
    time = 0
    # 증설된 시간 + k (종료시간), 증설 갯수 넣기
    server = deque()
    
    for player in players:
        # server 증설 끝나는 시간 체크
        if server and server[0][0] == time:
            a, b = server.popleft()
            n -= b
        
        capacity = n * m + m - 1
        # 만약 용량 초과하면
        if player > capacity:
            add = (player - capacity) // m
            capacity = (n+add) * m + m - 1
            
            if player != capacity:
                add += 1
            
            n += add
            server.append((time + k, add))
            answer += add
            
        time += 1
        print(server)
        print(n)
        print(capacity)
        print(player)
    return answer