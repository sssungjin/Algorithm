def solution(n, arr1, arr2):
    answer = [''] * n
    map1, map2 = [bin(i)[2:] for i in arr1], [bin(i)[2:] for i in arr2]
    
    idx = 0
    for i,j in zip(map1, map2):
        map1[idx] = i.zfill(n)
        map2[idx] = j.zfill(n)
        idx += 1
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer