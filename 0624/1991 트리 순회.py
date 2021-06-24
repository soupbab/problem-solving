import sys


def preorder_traversal(root):
    stack = []
    visited = []
    
    stack.append(root)
    
    while stack:
        node = stack.pop()
        visited.append(node)

        left = tree[node][0]
        right = tree[node][1]

        if right != ".":
            stack.append(right)
        if left != ".":
            stack.append(left)
        
    print("".join(visited))


def inorder_traversal(root):
    stack = []
    visited = []
    
    stack.append(root)
    
    while stack:
        node = stack[-1]

        left = tree[node][0]
        right = tree[node][1]

        if left != "." and left not in visited:
            stack.append(left)
        elif right != "." and right not in visited:
            visited.append(node)
            stack.pop()
            stack.append(right)

        if node == stack[-1]:
            visited.append(node)
            stack.pop()

    print("".join(visited))


def postorder_traversal(root):
    stack = []
    visited = []
    
    stack.append(root)
    
    while stack:
        node = stack[-1]

        left = tree[node][0]
        right = tree[node][1]

        if left != "." and left not in visited:
            stack.append(left)
        elif right != "." and right not in visited:
            stack.append(right)

        if node == stack[-1]:
            visited.append(node)
            stack.pop()

    print("".join(visited))


n = int(sys.stdin.readline().strip())
tree = {}
for _ in range(n):
    node, left, right = sys.stdin.readline().strip().split()
    tree[node] = [left, right]

root = "A"

preorder_traversal(root)
inorder_traversal(root)
postorder_traversal(root)
