import sys

sys.setrecursionlimit(10**6)

def solution(n):
    answer = []
    
    def recursion(n, start, end, extra):
        # 하나만 남아있으면 start에서 end로 옮기면 됨
        if n == 1:
            answer.append([start, end])
            return
        
        # 하나만 남아있는게 아니라면 먼저 n-1개까지 start에서 extra(중간)로 옮겨야함
        recursion(n -1, start, extra, end)
        
        # 옮기는 과정 기록
        answer.append([start, end])
        
        # 중간으로 옮겼다면 중간에서 end로 다시 옮김
        recursion(n-1, extra, end, start)
    
    recursion(n, 1, 3, 2)        
        
    
    return answer