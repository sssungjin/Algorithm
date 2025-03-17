word = input()

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ans = 0
while word != "":
    six_nine_chance = 2
    for i in num:
        if i in word:
            if i != '6' and i != '9':
                word = word.replace(i, "", 1)
            elif (i == '6' or i == '9'):
                word = word.replace(i, "", 1)
                six_nine_chance -= 1
    if six_nine_chance != 0 and '6' in word:
        word = word.replace('6', "", 1)
        six_nine_chance -= 1
    if six_nine_chance != 0 and '9' in word:
        word = word.replace('9', "", 1)
        six_nine_chance -= 1
    ans += 1
    
print(ans)