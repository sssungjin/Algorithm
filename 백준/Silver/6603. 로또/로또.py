def solution(arr, s, index, cnt):
    if cnt == 6:
        print(*arr)
        return
    
    for i in range(index, len(s)):
        arr[cnt] = s[i]
        solution(arr, s, i + 1, cnt + 1)


while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    arr = [0] * 6
    solution(arr, s[1:], 0, 0)
    print()
