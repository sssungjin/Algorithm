s = input()
length = len(s)
stk = []
tag = False
res = ''

for i in s:
    # 공백이면 stk에 들어있는거 pop해서 뒤집음
    if i == " ":
        while stk:
            res += stk.pop()
        res += i
    # 태그 시작하면 그 전까지 들어있던거 pop해서 뒤집고 < 삽입
    elif i == '<':
        while stk:
            res += stk.pop()
        tag = True
        res += i
    # 태그 끝나면 tag False로 바꾸고 > 기호 삽입
    elif i == '>':
        tag = False
        res += i
    # tag 안이면 뒤집지 않고 그냥 삽입
    elif tag:
        res += i
    else:
        stk.append(i)

while stk:
    res += stk.pop()

print(res)