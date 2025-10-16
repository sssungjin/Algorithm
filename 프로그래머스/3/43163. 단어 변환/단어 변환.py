# 현재 글자가 다른 글자와 한글자 차이나는지
def available(now_word, word):
    cnt = 0
    for i in range(len(now_word)):
        if now_word[i] != word[i]:
            cnt += 1
    
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    length = len(words)
    answer = float('inf')
    
    def dfs(now_word, cnt):
        nonlocal answer
        
        if cnt >= answer:
            return
        
        if now_word == target:
            answer = min(answer, cnt)
            return
        
        
        for i in range(length):
            if not visited[i] and available(now_word, words[i]):
                visited[i] = True
                dfs(words[i], cnt + 1)
                visited[i] = False
    
    dfs(begin, 0)
    
    return answer if answer != float('inf') else 0
            
