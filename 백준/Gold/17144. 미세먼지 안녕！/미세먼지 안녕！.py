# 모든 칸이 동시에 확산이 되어야 함 
# 미세먼지 있는 칸의 미세먼지 양, 좌표 넣어놓고
# 좌표가 c는 0이 아니고, 범위 안에 있으면 
# 그 부분에 Ar,c // 5  더해주고
# 더한칸 수만큼 원래 Ar,c에서 - 해줌
# 모든 좌표에 대해서 진행
# 이때 결과값은 원래 좌표 공간에다가 + 또는 - 처리해줌


# 미세먼지 처리
# r은 공기처리기 윗부분의 행 좌표
# 1초마다
# r 행에 있는 미세먼지는 오른쪽처리
# r + 1 행에 있는 미세먼지 오른쪽 처리
# c가 C - 1(맨 끝)이고, 0 <= x < r 이면 위로 
# c가 C - 1이고, r + 1 <= x < R 이면 아래로
# r이 0이면 왼쪽으로
# r이 R - 1 이면 왼쪽으로
# c는 0이고 0 <= x < r 이면 아래로
# c는 0이고 r + 1 <= x < R - 1 이면 위로

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
purifier = []

for r in range(R):
    if room[r][0] == -1:
        purifier.append(r)
        
def spread():
    changes = [[0] * C for _ in range(R)]
    
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                spread_amount = room[r][c] // 5
                spread_count = 0
                
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        changes[nr][nc] += spread_amount
                        spread_count += 1
                
                changes[r][c] -= spread_amount * spread_count
    
    for r in range(R):
        for c in range(C):
            room[r][c] += changes[r][c]
            
            

def run_purifier():
    
    up_r = purifier[0]
    
    # 아래로 이동
    for r in range(up_r - 1, 0, -1):
        room[r][0] = room[r-1][0]
    for c in range(0, C - 1):
        room[0][c] = room[0][c+1]
    for r in range(0, up_r):
        room[r][C-1] = room[r+1][C-1]
    for c in range(C - 1, 1, -1):
        room[up_r][c] = room[up_r][c-1]
    
    room[up_r][1] = 0
    
    down_r = purifier[1]
    
    for r in range(down_r + 1, R - 1):
        room[r][0] = room[r+1][0]
    for c in range(0, C - 1):
        room[R-1][c] = room[R-1][c+1]
    for r in range(R - 1, down_r, -1):
        room[r][C-1] = room[r-1][C-1]
    for c in range(C - 1, 1, -1):
        room[down_r][c] = room[down_r][c-1]
        
    room[down_r][1] = 0

for _ in range(T):
    spread()
    run_purifier()
    
    
total_dust = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            total_dust += room[r][c]
            
print(total_dust)