N = int(input())
tree = {}

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
# 0은 자신, 1은 왼쪽 자식, 2는 오른쪽 자식

def pre_order(root):
    if root == '.':
        return
    
    print(root, end='')
    pre_order(tree[root][0])
    pre_order(tree[root][1])
    
def mid_order(root):
    if root == '.':
        return
    
    mid_order(tree[root][0])
    print(root, end='')
    mid_order(tree[root][1])

def post_order(root):
    if root == '.':
        return
    
    post_order(tree[root][0])
    post_order(tree[root][1])
    print(root, end='')
    
pre_order('A')
print()
mid_order('A')
print()
post_order('A')