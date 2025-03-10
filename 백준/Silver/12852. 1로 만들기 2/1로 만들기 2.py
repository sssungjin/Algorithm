import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [-1] * 1000001

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = 0
    
    while queue:
        now, now_cnt = queue.popleft()
        
        if now == 1:
            # 경로 추적
            path = []
            current = 1
            while current != start:
                path.append(current)
                current = visited[current]
            path.append(start)
            path.reverse()
            return now_cnt, path

        for i in range(3):
            if i == 0 and now % 3 == 0 and visited[now // 3] == -1:
                visited[now // 3] = now 
                queue.append((now // 3, now_cnt + 1))
            elif i == 1 and now % 2 == 0 and visited[now // 2] == -1:
                visited[now // 2] = now
                queue.append((now // 2, now_cnt + 1))
            elif i == 2 and visited[now - 1] == -1:
                visited[now - 1] = now
                queue.append((now - 1, now_cnt + 1))

cnt, result = bfs(n)
print(cnt)
print(" ".join(map(str, result)))