import sys
from collections import deque


# def floid():
#     for i in range(n + 1):
#         for j in range(n + 1):
#             for k in range(n + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# if __name__ == "__main__":
#     n = int(input().strip())
#     a, b = map(int, input().strip().split())
#     m = int(input().strip())
#     graph = [[100 for _ in range(n + 1)] for _ in range(n + 1)]
#     for _ in range(m):
#         x, y = map(int, sys.stdin.readline().strip().split())
#         graph[x][y], graph[y][x] = 1, 1

#     floid()
#     print(graph[a][b] if graph[a][b] < 100 else -1)


def bfs():
    array = [-1] * (n + 1)
    q = deque([(a, 0)])
    while q:
        now, distance = q.popleft()

        for node in graph[now]:
            if array[node] == -1:
                array[node] = distance + 1
                q.append((node, distance + 1))

    print(array[b])


if __name__ == "__main__":
    n = int(input().strip())
    a, b = map(int, input().strip().split())
    m = int(input().strip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[x].append(y)
        graph[y].append(x)

    bfs()
    