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