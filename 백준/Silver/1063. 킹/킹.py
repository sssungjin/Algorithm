import sys
input = sys.stdin.readline

def AtoI(alpha):
    return ord(alpha) - ord('A') + 1

def ItoA(num):
    return chr(num + ord('A') - 1)

move_dict = {
    'R':  (0, 1),
    'L':  (0, -1),
    'B':  (-1, 0),
    'T':  (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

king, stone, n = input().split()
n = int(n)

commands = [input().strip() for _ in range(n)]

king_r = int(king[1])
king_c = AtoI(king[0])

stone_r = int(stone[1])
stone_c = AtoI(stone[0])

for cmd in commands:
    if cmd not in move_dict:
        continue
    dr, dc = move_dict[cmd]

    next_king_r = king_r + dr
    next_king_c = king_c + dc

    # 킹이 체스판 벗어나면 무시
    if not (1 <= next_king_r <= 8 and 1 <= next_king_c <= 8):
        continue

    # 킹 이동했을 때 돌이 있으면 돌도 같은 방향으로
    if next_king_r == stone_r and next_king_c == stone_c:
        next_stone_r = stone_r + dr
        next_stone_c = stone_c + dc

        # 돌이 체스판 벗어나면 둘 다 이동 안 함
        if not (1 <= next_stone_r <= 8 and 1 <= next_stone_c <= 8):
            continue

        # 둘 다 이동
        king_r, king_c = next_king_r, next_king_c
        stone_r, stone_c = next_stone_r, next_stone_c
    else:
        # 돌이 없으면 킹만 이동
        king_r, king_c = next_king_r, next_king_c

print(ItoA(king_c) + str(king_r))
print(ItoA(stone_c) + str(stone_r))
