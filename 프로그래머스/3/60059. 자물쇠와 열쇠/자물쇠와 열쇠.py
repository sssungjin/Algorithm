# 90도 회전
def rotate(key):
    return list(zip(*key[::-1]))
# 열쇠 넣기 (이동)
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]
    
# 열쇠 빼기 (이동 복구)
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]
            
# 열쇠가 lock 에 맞는지 확인
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True        

def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * (M * 2 + N) for _ in range(M*2 + N)]
    
    # 자물쇠를 중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
            
    #모든 방향 회전
    for _ in range(4):
        key = rotate(key)
        # 이동 시켜서 넣어보기
        for x in range(1, M + N):
            for y in range(1, M + N):
                attach(x, y, M, key, board)
                if(check(board, M, N)):
                    return True
                detach(x, y, M, key, board)
                
    return False