def check(board):
    bingo = 0
    for i in range(5):
        if board[i][0] == 0 and board[i][1] == 0 and board[i][2] == 0 and board[i][3] == 0 and board[i][4] == 0:
            bingo += 1
        if board[0][i] == 0 and board[1][i] == 0 and board[2][i] == 0 and board[3][i] == 0 and board[4][i] == 0:
            bingo += 1
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
        bingo += 1
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
        bingo += 1
    
    return bingo

def main():
    board = []
    nums = []

    for _ in range(5):
        board.append(list(map(int, input().split())))

    for _ in range(5):
        nums.extend(list(map(int, input().split())))
    cnt = 0
    for num in nums:
        cnt += 1
        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    board[i][j] = 0
                    if check(board) >= 3:
                        print(cnt)
                        return

if __name__ == "__main__":
    main()

