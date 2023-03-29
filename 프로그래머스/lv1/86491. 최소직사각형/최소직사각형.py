def solution(sizes):
    width,height = 0, 0
    lst = []
    for i in sizes:
        lst.append(sorted(i))
    for i in lst:
        width = max(width, i[0])
        height = max(height, i[1])
    return width * height