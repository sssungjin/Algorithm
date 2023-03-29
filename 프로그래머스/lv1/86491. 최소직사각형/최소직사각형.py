def solution(sizes):
    answer = 0
    width,height = 0, 0
    lst = []
    for i in sizes:
        lst.append(sorted(i))
    for i in lst:
        width = max(width, i[0])
        height = max(height, i[1])
    answer = width * height
    return answer