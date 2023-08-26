def solution(sequence, k):
    answer, n, idx = [], sequence[0], 0
    for i, v in enumerate(sequence):
        # 합(n)이 k 보다 작을 때
        while n < k and idx <= len(sequence) - 2:
            idx += 1
            n += sequence[idx]
        # 합이 더 커서 while 종료 후 확인
        if n == k:
            answer.append([idx - i, [i, idx]])
        #가장 앞에걸 하나씩 빼주면서 다 확인
        n -= v
    answer.sort() #길이 기준 정렬 후 반환
    return answer[0][1]