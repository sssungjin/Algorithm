N = int(input())
graph = [[] * N for _ in range(N)]

for i in range(N):
    line = input()
    for j in range(N):
        c = int(line[j])
        graph[i].append(c)
        
def quad(r, c, length):
    color = graph[r][c]
    same = True
    
    # if length == 2:
    #     values = [
    #         graph[r][c],
    #         graph[r][c + length],
    #         graph[r + length][c],
    #         graph[r][c + length]
    #     ]
    #     flag = True
    #     for i in range(4):
    #         if values[i] != color:
    #             flag = False
    #             break
    #     if flag == True:
    #         print(color)
    #     else:
    #         print("(" , values, ")", sep='')
    
    for i in range(r, r + length):
        for j in range(c, c + length):
            if graph[i][j] != color:
                same = False
                break
        if not same:
            break
    
    if same:
        return str(color)
    
    half = length // 2
    top_left = quad(r, c, half)
    top_right = quad(r, c + half, half)
    bottom_left = quad(r + half, c, half)
    bottom_right = quad(r + half, c + half, half)
    
    return "(" + top_left + top_right + bottom_left + bottom_right + ")"

print(quad(0, 0, N))