for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    data = []
    idx = 0
    for i in range(n):
        data.append(arr[idx:idx+m])
        idx += m
    
    # 두번째 열부터 확인
    for j in range(1, m):
        for i in range(n):
            # 첫번째 행인 경우 왼쪽 위에서는 올 수 없음
            if i == 0:
                left_up = 0
            else:
                left_up = data[i-1][j-1]
            # 마지막 행인 경우 아래에서 올 수 없음
            if i == n - 1:
                left_down = 0
            else: 
                left_down = data[i+1][j-1]
            left = data[i][j-1]
            data[i][j] = data[i][j] + max(left_up, left_down, left)

    result = 0
    # 각 행의 마지막 값 중 최댓값 저장
    for i in range(n):
        result = max(result, data[i][m-1])
    print(result)

