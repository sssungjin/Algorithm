def check_square(x, y, mat, park):
    for i in range(y, y + mat):
        for j in range(x, x + mat):
            if park[i][j] != '-1':
                return 0
    return mat

def solution(mats, park):
    width = len(park[0])
    height = len(park)
    
    mats.sort(reverse=True)
    
    for mat_size in mats:
        for y in range(height - mat_size + 1):
            for x in range(width - mat_size + 1):
                possible_mat_size = check_square(x, y, mat_size, park)
                if possible_mat_size > 0:
                    return mat_size

    return -1