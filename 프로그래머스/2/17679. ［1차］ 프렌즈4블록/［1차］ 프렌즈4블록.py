def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    while True:
        remove_set = set()
        
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == ' ':
                    continue
                if block == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    remove_set.add((i, j))
                    remove_set.add((i, j + 1))
                    remove_set.add((i + 1, j))
                    remove_set.add((i + 1, j + 1))
        
        if not remove_set:
            break
        
        for i, j in remove_set:
            board[i][j] = ' '
        answer += len(remove_set)
        
        for j in range(n):
            empty = []
            for i in reversed(range(m)):
                if board[i][j] == ' ':
                    empty.append(i)
                elif empty:
                    target = empty.pop(0)
                    board[target][j] = board[i][j]
                    board[i][j] = ' '
                    empty.append(i)
                    
                    
    return answer