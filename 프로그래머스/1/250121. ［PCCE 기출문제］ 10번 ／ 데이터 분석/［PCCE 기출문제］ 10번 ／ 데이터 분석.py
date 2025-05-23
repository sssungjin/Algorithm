def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    # ext 해당 데이터 값 < val_ext
    # code: 0, date: 1, maximum: 2, remain: 3
    # sort_by 로 정렬
    answer = []
    
    ext_idx, sort_idx = 0, 0
    
    if ext == 'code':
        ext_idx = 0
    elif ext == 'date':
        ext_idx = 1
    elif ext == 'maximum':
        ext_idx = 2
    elif ext == 'remain':
        ext_idx = 3
    
    if sort_by == 'code':
        sort_idx = 0
    elif sort_by == 'date':
        sort_idx = 1
    elif sort_by == 'maximum':
        sort_idx = 2
    elif sort_by == 'remain':
        sort_idx = 3
    
    for i in data:
        if i[ext_idx] < val_ext:
            answer.append(i)
            
    answer.sort(key = lambda x: (x[sort_idx], x[0]))
    
    return answer