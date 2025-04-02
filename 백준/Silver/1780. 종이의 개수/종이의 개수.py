N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]

def cut(size, r, c):
    value = paper[r][c]
    
    flag = True
    for i in range(r, r + size):
        for j in range(c, c + size):
            if paper[i][j] != value:
                flag = False
                break
        if not flag:
            break
        
    
    if flag:
        ans[value + 1] += 1
    else:
        third = size // 3
        cut(third, r, c)
        cut(third, r + third, c)
        cut(third, r, c + third)
        cut(third, r + third, c + third)
        cut(third, r + third * 2, c)
        cut(third, r, c + third * 2)
        cut(third, r + third, c + third * 2)
        cut(third, r + third * 2, c + third)
        cut(third, r + third * 2, c + third * 2)

cut(N, 0, 0)

for i in ans:
    print(i)