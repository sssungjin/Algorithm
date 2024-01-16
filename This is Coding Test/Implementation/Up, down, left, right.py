def travel(N, plans):
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    
    for move in plans:
        for i in range(len(move_types)):
            if move == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        x, y = nx, ny
    print(x, y)

def main():
    N = int(input())
    plans = input().split()
    travel(N, plans)

if __name__ == "__main__":
    main()