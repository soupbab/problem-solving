import sys


def floid():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] == 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for row in graph[1:]:
        for cost in row[1:]:
            print(cost if cost != INF else 0, end=" ")
        print()


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    INF = 1e9
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = min(graph[a][b], c)

    floid()
