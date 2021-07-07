import sys


def floyd(table):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if table[i][k] == True and table[k][j] == True:
                    table[i][j] = True


def main():
    floyd(graph_a)
    floyd(graph_b)

    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i - 1][j - 1] = True
            elif graph_a[i][j] == True or graph_b[i][j] == True:
                graph[i - 1][j - 1] = True

    count = 0
    for row in graph:
        if False not in row:
            count += 1

    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph_a = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    graph_b = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph_a[a][b] = True
        graph_b[b][a] = True

    main()
