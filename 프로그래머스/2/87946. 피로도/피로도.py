answer = 0

def back_tracking(k, cnt, dungeons, visited):
    global answer 
    answer = max(answer, cnt)
    
    # 만약 최소 필요 피로도보다 현재 피로도가 크고 지금 루프에서 방문하지 않았다면
    # 피로도 차감, cnt +1
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k and not visited[i]:
            visited[i] = True
            back_tracking(k - dungeons[i][1], cnt + 1, dungeons, visited)
            # 함수가 끝나면 방문 안함 처리
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    back_tracking(k, 0, dungeons, visited)
    
    return answer