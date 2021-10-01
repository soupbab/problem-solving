def solution(m, n, puddles):
    graph = [[-1 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        x, y = puddle
        graph[y - 1][x - 1] = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                continue
                
            if y == 0 and x == 0:
                graph[y][x] = 1
            elif y == 0:
                graph[y][x] = graph[y][x - 1]
            elif x == 0:
                graph[y][x] = graph[y - 1][x]
            else:
                graph[y][x] = graph[y][x - 1] + graph[y - 1][x]

    return graph[n - 1][m - 1] % 1000000007
