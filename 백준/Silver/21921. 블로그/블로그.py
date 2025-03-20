n, x = map(int, input().split())
visitors = list(map(int, input().split()))
window_size = n - x + 1

window = [0] * window_size
window[0] = sum(visitors[0:x])
max_window = window[0]
cnt = 1

for i in range(1, window_size):
    window[i] = window[i - 1] + visitors[i + x - 1] - visitors[i - 1]

    if window[i] > max_window:
        max_window = window[i]
        cnt = 1
    elif window[i] == max_window:
        cnt += 1

if max_window == 0:
    print("SAD")
else:
    print(max_window)
    print(cnt)