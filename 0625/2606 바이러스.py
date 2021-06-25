import sys


def merge(a, b):
    parent = min(parents[a], parents[b])
    parents[a] = parent
    parents[b] = parent


def search(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = search(parents[a])
        return parents[a]


def union_find(a, b):
    parent_a = search(a)
    parent_b = search(b)

    merge(parent_a, parent_b)


def renewal():
    for i in range(1, n + 1):
        parents[i] = search(i)


if __name__ == "__main__":
    n = int(input().strip())
    l = int(input().strip())
    parents = [i for i in range(n + 1)]

    for _ in range(l):
        a, b = map(int, sys.stdin.readline().strip().split())
        union_find(a, b)

    renewal()
    print(parents)
    # print(parents.count(1) - 1)
