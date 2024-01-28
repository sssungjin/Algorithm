def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    ans = []
    # 부모를 자기 자신으로 초기화
    for i in range(0, n + 1):
        parent[i] = i
    
    for i in range(m):
        op, a, b = map(int, input().split())
        # union 실행
        if op == 0:
            union_parent(parent, a, b)
        elif op == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                ans.append("YES")
            else:
                ans.append("NO")
    for i in ans:
        print(i)

if __name__ == "__main__":
    main()