def quad(i, j, size, arr, answer):
    first = arr[i][j]
    flag = True
    
    for x in range(i, i + size):
        for y in range(j, j + size):
            if arr[x][y] != first:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        answer[first] += 1
    else:
        half = size // 2
        quad(i, j, half, arr, answer)
        quad(i + half, j, half, arr, answer)
        quad(i, j + half, half, arr, answer)
        quad(i + half, j + half, half, arr, answer)

def solution(arr):
    answer = [0, 0]
    
    quad(0, 0, len(arr), arr, answer)
            
    
    return answer