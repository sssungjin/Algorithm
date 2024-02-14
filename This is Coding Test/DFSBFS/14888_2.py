n = int(input()) 
array = list(map(int,input().split())) 
add, sub, mul, div = map(int,input().split()) 

max_value = -1e9 - 1
min_value = 1e9 + 1

def dfs(i, now):
    global add, sub, mul, div, max_value, min_value

    if i == n: 
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0: # 더하기 연산자가 1개 이상이면
            add -= 1 # 연산할 것이므로 한개 빼주고
            dfs(i + 1, now + array[i]) # 다음 연산할 index와 계산 결과 넘겨줌
            add += 1 # 모두 완료하면 다시 연산자의 개수 돌려줌
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - array[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * array[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / array[i])) 
            div += 1

dfs(1, array[0])

print(max_value)
print(min_value)