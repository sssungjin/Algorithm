N = int(input())
commands = input()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

direction = 2

r, c = 0, 0
history = {(0, 0)}

for cmd in commands:
    if cmd == 'F':
        r, c = r + dr[direction], c + dc[direction]
        history.add((r, c))
    elif cmd == 'L':
        direction = (direction - 1 + 4) % 4
    elif cmd == 'R':
        direction = (direction + 1) % 4

min_r = min(item[0] for item in history)
min_c = min(item[1] for item in history)

maze_coords = set()
for r, c in history:
    maze_coords.add((r - min_r, c - min_c))

max_r = max(item[0] for item in maze_coords)
max_c = max(item[1] for item in maze_coords)

maze_grid = [['#'] * (max_c + 1) for _ in range(max_r + 1)]

for r, c in maze_coords:
    maze_grid[r][c] = '.'

for row in maze_grid:
    print("".join(row))