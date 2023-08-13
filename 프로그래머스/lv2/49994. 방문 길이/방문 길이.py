def solution(dirs):
    dic = {'R': (0,1), 'L': (0,-1), 'U': (1,0), 'D': (-1,0)}
    sets = set()
    #좌상단을 0,0
    #원점을 5,5라고 가정
    x, y = 5, 5
    for i in dirs:
        dy, dx = dic[i]
        ny = y + dy
        nx = x + dx
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            # 경로 알기 위해 전 위치와 움직일 위치 같이 저장
            sets.add(((y, x), (ny, nx)))
            # 반대도 저장
            sets.add(((ny, nx), (y, x)))
            y = ny
            x = nx
    # 2개의 원소(좌표) 하나 = 길이 1
    return len(sets) // 2
