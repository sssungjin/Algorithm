n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
answer = 0
def back_tracking(li):
    global answer
    # 배열이 꽉 찼다면
    if len(li) == n:
        total = 0
        # total 값을 구함
        for i in range(n - 1):
            total += abs(li[i] - li[i+1])
        # total이 더 크면 answer에 저장
        answer = max(answer, total)
        return
    
    # 방문 처리 후 재귀 호출, 완료되면 미방문 처리 하고 pop
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            li.append(arr[i])
            back_tracking(li)
            visited[i] = False
            li.pop()

back_tracking([])
print(answer)
