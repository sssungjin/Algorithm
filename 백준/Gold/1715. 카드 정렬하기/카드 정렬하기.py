from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()
answer = 0

for _ in range(n):
    queue.put(int(input()))

while queue.qsize() > 1:
    a = queue.get()
    b = queue.get()
    answer += a + b
    queue.put(a+b)

print(answer)