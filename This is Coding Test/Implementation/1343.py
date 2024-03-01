board = list(input())

# A를 먼저 놔보고 안된다면 B, 둘다 안되면 -1

idx = 0
while idx <= len(board) - 1:
    if board[idx] == 'X':
        length = 0
        # X의 길이를 구함
        for i in range(idx, len(board)):
            if board[i] == '.':
                break
            else:
                length += 1
        if length % 2 != 0:
            print('-1')
            break
        # A블럭의 개수
        a_block = length // 4
        # B블럭은 4로 안나눠질때만 마지막에 하나 배치
        if length % 4 != 0:
            # A블럭 배치
            for k in range(idx, idx + length - 2):
                board[k] = 'A'
            # B블럭 배치
            for k in range(idx + length - 2, idx + length):
                board[k] = 'B'
        else:
            for k in range(idx, idx + length):
                board[k] = 'A'
        idx += length
    else:
        idx += 1
        continue
else:
    print(''.join(board))