def check(word):
    stk = []
    
    for i in range(len(word)):
        if len(stk) == 0 or stk[-1] != word[i]:
            stk.append(word[i])
        else:
            stk.pop()

    if len(stk) != 0:
        return False
    else:
        return True

n = int(input())
words = [input() for _ in range(n)]
answer = 0
for word in words:
    if check(word):
        answer += 1

print(answer)