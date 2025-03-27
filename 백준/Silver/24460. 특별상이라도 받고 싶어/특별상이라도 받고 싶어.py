import sys
sys.setrecursionlimit(10**6)

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

def recursion(size, r, c):
    if size == 1:
        return map[r][c]
    else:
        values = [
            recursion(size // 2, r, c),
            recursion(size // 2, r + size // 2, c),
            recursion(size // 2, r, c + size // 2),
            recursion(size // 2, r + size // 2, c + size // 2)
        ]
        return sorted(values)[1]
        
print(recursion(N, 0, 0))