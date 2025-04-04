K = int(input())
sequence = list(map(int, input().split()))

levels = [[] for _ in range(K + 1)]

def dfs(sequence, level):
    mid = len(sequence) // 2
    
    levels[level].append(sequence[mid])
    
    if len(sequence) == 1:
        return
    
    dfs(sequence[:mid], level + 1)
    dfs(sequence[mid+1:], level + 1)
    
dfs(sequence, 0)

for i in levels:
    print(*i)
    