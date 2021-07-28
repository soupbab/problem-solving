import sys
from collections import deque


def dfs(root, tree):
    count = 0

    q = deque([root])
    while q:
        node = q.popleft()
        children = tree[node]
        if children:
            q.extend(tree[node])
        else:
            count += 1

    return count


def main():
    root = parent.index(-1)
    tree = [[] for _ in range(n)]
    for i in range(n):
        if i != target and parent[i] != -1:
            tree[parent[i]].append(i)

    if target == root:
        leaf = 0
    else:
        leaf = dfs(root, tree)

    print(leaf)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    parent = list(map(int, input().split()))
    target = int(input())

    main()
