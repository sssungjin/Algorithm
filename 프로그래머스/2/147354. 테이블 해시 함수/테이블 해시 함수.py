def solution(data, col, row_begin, row_end):
    answer = 0
    # col 번째 컬럼의 값을 기준으로 오름차순 정렬, 첫번째 컬럼 값 기준으로 내림차순 정렬
    # i번째 행의 데이터를 i로 나눈 값은 S_i
    # row_begin ~ row_end 의 S_i를 누적하여 bitwise XOR 값 반환
    if col >= 2:
        data.sort(key = lambda x: (x[col - 1], -x[0]))
    else:
        data.sort()
    
    S_row = []
    for row_idx in range(row_begin - 1, row_end):
        S = 0
        row = data[row_idx]
        for value in row:
            S += value % (row_idx + 1)
        S_row.append(S)
        
    answer = 0
    
    for val in S_row:
        answer = answer ^ val
        
    return answer