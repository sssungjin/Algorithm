# 중요도를 확인해서 중요도가 더 높은게 있다면 맨 뒤에 배치
# 중요도가 모두 다 낮다면 인쇄
# 같은게 있을 수 있으므로 정렬 사용 불가능

def solution(n, target_idx, arr):
    queue = []
    answer = []
    for i in range(len(arr)):
        # 문서의 처음 인덱스와 중요도를 큐에 순서대로 저장
        queue.append([i, arr[i]])
    
    flag = False
    while queue:
        i, importance = queue.pop(0)
        for idx, imp in queue:
            if imp > importance:
                queue.append([i, importance])
                break
        else:
            answer.append([i, importance])
    for i in range(len(answer)):
        if answer[i][0] == target_idx:
            return i + 1

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(n, m, arr))