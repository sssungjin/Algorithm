n, k = map(int, input().split())
arr = list(input())
eaten = [False] * n
cnt = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            # 범위 밖이거나 자신
            if j < 0 or j >= n or j == i:
                continue
            if arr[j] == 'H' and not eaten[j]:
                eaten[j] = True
                cnt += 1
                break

print(cnt)