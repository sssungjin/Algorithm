def solution(dirs):
    answer = 0
    visited_paths = set()
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    move_types = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
    
    now_r, now_c = 5, 5
    
    for cmd in dirs:
        move_idx = move_types[cmd]
        next_r, next_c = now_r + dr[move_idx], now_c + dc[move_idx]
        
        if not (0 <= next_r <= 10 and 0 <= next_c <= 10):
            continue
            
        path1 = (now_r, now_c, next_r, next_c)
        path2 = (next_r, next_c, now_r, now_c)
        
        if path1 not in visited_paths:
            visited_paths.add(path1)
            visited_paths.add(path2)
            answer += 1
            
        now_r, now_c = next_r, next_c
            
    return answer