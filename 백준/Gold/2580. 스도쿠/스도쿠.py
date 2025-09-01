SIZE = 9
sudoku = [list(map(int, input().split())) for _ in range(SIZE)]

# 빈칸 좌표 (행, 열)
blank_coord = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]

def check(y, x, n):
    BOX_SIZE = 3
    
    for i in range(SIZE):
        if sudoku[y][i] == n or sudoku[i][x] == n:
            return False
    
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == n:
                return False
    return True

def solution(n):
    if n == len(blank_coord):
        for i in sudoku:
            print(*i)
        exit()
    
    for check_num in range(1, 10):
        y, x = blank_coord[n]
        
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            solution(n + 1)
            sudoku[y][x] = 0

solution(0)