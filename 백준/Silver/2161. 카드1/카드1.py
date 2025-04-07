from collections import deque
N = int(input())

queue = deque([i for i in range(1, N + 1)])
arr = []

while len(queue) > 1:
    arr.append(queue.popleft()) # 버리기
    queue.append(queue.popleft()) # 뒤로 옮기기기
    
arr.append(queue.popleft())

print(' '.join(map(str, arr)))
    