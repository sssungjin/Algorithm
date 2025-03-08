# 총 층수, 현재 층수, 목표 층수, 위로 이동 가능 층수, 아래로 이동 가능 층수

from collections import deque

f, start, target, u, d = map(int, input().split())

visited = [0] * (f + 1)

move = [u, d * -1]

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    
    while queue:
        now = queue.popleft()
        
        if now == target:
            return visited[now] - 1
        
        for i in move:
            next = now + i
            
            if 1 <= next <= f and visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)
    
    return -1

result = bfs(start)

if result == -1:
    print("use the stairs")
else:
    print(result)