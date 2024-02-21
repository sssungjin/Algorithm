import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
l1, l2 = len(word1), len(word2)
cache = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1,l1 + 1):
    for j in range(1,l2 + 1):
        # 같으면 +1
        if word1[i - 1] == word2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
print(cache)
print(cache[-1][-1])