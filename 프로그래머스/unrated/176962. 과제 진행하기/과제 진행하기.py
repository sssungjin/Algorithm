def solution(plans):
    answer = []
    #정수 변환
    for time in plans:
        time[2] = int(time[2])
        time[1] = int(time[1][0:2]) * 60 + int(time[1][3:5])
    plans.sort(key=lambda x:x[1])
    stack = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break
        csubject, cstart, ctime = plans[i]
        nsubject, nstart, ntime = plans[i+1] 
        
        if cstart + ctime <= nstart:
            answer.append(csubject)
            #문제 풀고 다음 과제 시작까지 남은시간 있으면 스택에 있던 과제 수행
            remain = nstart - cstart - ctime
            
            while remain != 0 and stack:
                st_subject, st_start, st_time = stack.pop()
                #남은시간이 스택에 들어있는 과제의 필요시간보다 크면
                if remain >= st_time:
                    answer.append(st_subject)
                    remain -= st_time
                else:
                    stack.append([st_subject, st_start, st_time - remain])
                    remain = 0
        #다음과제 시작할 때까지 시간이 모자른 경우 진행한 시간 빼고 스택에 넣음    
        else: 
            plans[i][2] = ctime - (nstart - cstart)
            stack.append(plans[i])
    
    while stack:
        answer.append(stack.pop()[0])
    return answer