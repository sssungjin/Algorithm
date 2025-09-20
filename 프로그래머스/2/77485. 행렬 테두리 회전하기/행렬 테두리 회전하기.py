# solution 함수는 기존 코드와 거의 동일합니다.
def solution(rows, columns, queries):
    answer = []
    graph = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        rotate_clock(graph, x1, y1, x2, y2, answer)
    
    return answer

def rotate_clock(graph, x1, y1, x2, y2, answer):
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    
    temp = graph[x1][y1]
    
    min_value = temp
    
    # 왼쪽 세로줄 (아래 값을 위로 당겨옴)
    for i in range(x1, x2):
        value = graph[i + 1][y1]
        graph[i][y1] = value
        min_value = min(min_value, value)

    # 아래 가로줄 (오른쪽 값을 왼쪽으로 당겨옴)
    for j in range(y1, y2):
        value = graph[x2][j + 1]
        graph[x2][j] = value
        min_value = min(min_value, value)

    # 오른쪽 세로줄 (위 값을 아래로 당겨옴)
    for i in range(x2, x1, -1):
        value = graph[i - 1][y2]
        graph[i][y2] = value
        min_value = min(min_value, value)

    # 위쪽 가로줄 (왼쪽 값을 오른쪽으로 당겨옴)
    for j in range(y2, y1, -1):
        value = graph[x1][j - 1]
        graph[x1][j] = value
        min_value = min(min_value, value)
        
    graph[x1][y1 + 1] = temp
    
    answer.append(min_value)
    
    return