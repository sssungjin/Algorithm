N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

def sol(length, r, c):
    color = graph[r][c]
    for i in range(r, r + length):
        for j in range(c, c + length):
            if color != graph[i][j]:
                next_length = length // 2
                sol(next_length, r, c)
                sol(next_length, r, c + next_length)
                sol(next_length, r + next_length, c)
                sol(next_length, r + next_length, c + next_length)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1
    

sol(N, 0, 0)   
print(result[0], '\n', result[1], sep='')    
    