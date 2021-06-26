import sys
from collections import deque


def find_parents():
    q = deque([1])

    while q:
        now = q.popleft()

        for node in links[now]:
            if parents[node] == 0:
                parents[node] = now
                q.append(node)


if __name__ == "__main__":
    n = int(input().strip())
    links = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        links[a].append(b)
        links[b].append(a)

    parents = [0] * (n + 1)

    find_parents()

    for i in range(n - 1):
        print(parents[i + 2])
    