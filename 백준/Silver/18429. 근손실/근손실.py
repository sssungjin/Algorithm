N, m = map(int, input().split())
a = list(map(int, input().split()))
visited = [False] * N
ans = 0

def dfs(n, weight):
    global ans
    if weight < 500:
        return
    
    if n == N:
        ans += 1
        return
    
    weight -= m
    for i in range(N):
       if visited[i]:
           continue
       
       visited[i] = True
       dfs(n + 1, weight + a[i])
       visited[i] = False 
       
       
dfs(0, 500)
print(ans)