n, m = map(int, input().split())
arr = []

def solution(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n+1):
        arr.append(i)
        solution(i)
        arr.pop()

solution(1)