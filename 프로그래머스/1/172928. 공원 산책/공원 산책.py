def solution(park, routes):
    answer = []
    # 이동 중에 장애물 만나거나 맵 밖으로 나가면 수행 X -> 다음꺼 수행
    # E W S N
    directions = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}
    
    width = len(park[0])
    height = len(park)
    
    r, c = 0, 0
    
    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                r, c = i, j # r, c
    nr, nc = 0, 0
    
    for cmd in routes:
        direction, dist_str = cmd.split()
        dist = int(dist_str)
        dr_val, dc_val = directions[direction]
        
        current_r, current_c = r, c
        is_possible = True
        
        for step in range(dist):
            nr, nc = current_r + dr_val, current_c + dc_val
            
            if not(0 <= nr < height and 0 <= nc < width):
                is_possible = False
                break
            
            if park[nr][nc] == 'X':
                is_possible = False
                break
        
            current_r, current_c = nr, nc
        
        if is_possible:
            r, c = current_r, current_c
                
    return [r, c]