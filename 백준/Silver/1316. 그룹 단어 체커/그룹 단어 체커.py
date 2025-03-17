n = int(input())
words = [input() for _ in range(n)]
cnt = 0

for word in words:
    seen = set()
    is_group_word = True
    for i in range(len(word)):
        if word[i] in seen:
            if word[i] != word[i - 1]:
                is_group_word = False
                break
        else:
            seen.add(word[i])
    if is_group_word:
        cnt += 1

print(cnt)