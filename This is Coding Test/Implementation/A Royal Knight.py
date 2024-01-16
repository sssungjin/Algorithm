def solution(N):
    x, y = ord(N[0]) - 96, int(N[1])
    # x 좌표는 a,b,c... y 좌표는 1,2,3..
    
    dx = [2, 2, -2, -2, -1, 1, -1, 1] 
    dy = [-1, 1, -1, -1, 2, 2, -2, -2] 
    move_types = [
    'RU', 'RD', 'LU', 'LD','DL', 'DR', 'UL', 'UR']

    ans = 0

    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        ans += 1

def main():
    N = input()
    solution(N)

if __name__ == "__main__":
    main()