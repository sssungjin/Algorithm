def solution(m, musicinfos):
    answer = []
    # '#' 치환
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    idx = 0
    for i in musicinfos:
        start, end, title, code = i.split(',')
        
        #시간 계산
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))
        start_time = start_hour * 60 + start_minute
        end_time = end_hour * 60 + end_minute
        
        # '#' 치환
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        time = end_time - start_time
        played_code = code * (time // len(code)) + code[:time % len(code)]
        
        if m in played_code:
            answer.append([title, time, idx])
            idx += 1
            
    if not answer:
        return "(None)"
    else:
        # 재생 시간은 내림차순, 인덱스는 오름차순으로 정렬
        answer = sorted(answer, key=lambda x: (-x[1], x[2]))
        return answer[0][0]
