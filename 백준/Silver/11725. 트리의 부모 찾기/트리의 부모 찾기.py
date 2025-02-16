from collections import deque
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 2차원 배열 생성
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

parent = [0] * (n + 1)

def bfs():
    q = deque([1])
    
    while q:
        # 현재 노드
        node = q.popleft()
        # 현재 노드와 연결된 모든 노드 확인
        for neighbor in graph[node]:
            # 부모가 정해지지 않은 경우
            if parent[neighbor] == 0:
                # 연결된 노드의 부모는 현재 노드
                parent[neighbor] = node
                q.append(neighbor)
                
bfs()
for i in range(2, n + 1):
    print(parent[i])