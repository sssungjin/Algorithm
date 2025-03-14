n = int(input())

tmp = n
cnt = 0

while True:
    first = tmp // 10
    second = tmp % 10
    third = (first + second) % 10
    tmp = second * 10 + third
    cnt += 1
    if tmp == n:
        break

print(cnt)