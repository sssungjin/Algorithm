
n, k = map(int, input().split())

queue = [i for i in range(1, n + 1)]

idx = 0
ans = []

while queue:
    idx = (idx + (k - 1)) % len(queue)
    ans.append(queue[idx])
    del queue[idx]

print("<" + ", ".join(map(str, ans)) + ">")