import sys
import heapq


def main():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if k == i:
                continue
            for j in range(1, n + 1):
                if k == j:
                    continue

                if i == j:
                    graph[i][j] = 0
                else:
                    if graph[i][k] != INF and graph[k][j] != INF:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for k in range(2, n + 1):
        for i in range(1, n + 1):
            if k == i:
                continue

            if graph[1][k] != INF and graph[k][i] != INF:
                if graph[1][i] > graph[1][k] + graph[k][i]:
                    print(-1)
                    return  

    for dist in graph[1][2:]:
        print(dist if dist != INF else -1)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    INF = 1e9
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = min(graph[a][b], c)

    main()

# def main(start):
#     INF = 1e9
#     distances = [INF] * (n + 1)
#     distances[start] = 0

#     for _ in range(n - 1):
#         for i in range(1, n + 1):
#             for node, dist in graph[i]:
#                 if distances[i] != INF:
#                     cost = dist + distances[i]
#                     if distances[node] > cost:
#                         distances[node] = cost

#     for node, dist in graph[1]:
#         cost = dist + distances[1]
#         if distances[node] > cost:
#             print(-1)
#             break
#     else:
#         for distance in distances[2:]:
#             print(distance if distance != INF else -1)


# if __name__ == "__main__":
#     n, m = map(int, sys.stdin.readline().strip().split())
#     graph = [[] for _ in range(n + 1)]
#     for _ in range(m):
#         a, b, c = map(int, sys.stdin.readline().strip().split())
#         graph[a].append((b, c))

#     start = 1
#     main(start)
