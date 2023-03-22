def solution(id_list, report, k):
    #key: 신고당한 사람(문자열), value: 신고한 사람 배열
    rep_info = {}
    #key : 메시지 받을 사람(문자열) value: 받을 횟수(정수)
    msg = {}
    lst = []
    tmp = []
    for i in id_list:
        rep_info[i] = []
        msg[i] = 0
        
    # for i in id_list:
    #     for j in set(report):
    #     #report 문자열 공백 뒤 확인해서 존재하면 rep_info에 저장            
    #     #신고당한 유저 id를 키, 신고한 유저 id를 value
    #     #value 중복 제거 후 신고 당한 횟수는 value의 len
    #         tmp = list(j.split())
    #         if i == tmp[1]:
    #             lst.append(tmp[0])
    #     rep_info[i] = lst[:]
    #     lst = []
        
    for r in report:
        s,t = r.split()
        if s not in rep_info[t]:
            rep_info[t].append(s)
            
        
        #rep_info 확인해서 길이가 k 이상이면 정지
        #메시지 보내기 위해서 k이상이면 rep_info의 value 확인해서 신고한 사람들을
        #새로운 딕셔너리 msg[신고한 사람] = 메시지 받을 횟수 로 저장
    for i in id_list:
        if len(rep_info[i]) >= k:
            for j in rep_info[i]:
                msg[j] += 1
                
    return list(msg.values())