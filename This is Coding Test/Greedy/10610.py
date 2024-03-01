n = list(map(int, input()))

n.sort(reverse = True)

# 10의 배수인지 확인
if 0 not in n:
    print(-1)
else:
    # 합이 3의 배수가 아니면 num은 3의 배수가 아님
    if sum(n) % 3 != 0:
        print(-1)
    else:
        answer = ''.join(map(str, n))
        print(answer)
