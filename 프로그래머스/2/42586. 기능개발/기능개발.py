def solution(progresses, speeds):
    answer = []
    time, count = 1, 0
    
    while progresses:
        # 작업 완료 했다면 pop
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer