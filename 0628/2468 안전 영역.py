import sys
sys.setrecursionlimit(15000)
from collections import deque
from copy import deepcopy


def dfs(x, y, rain):
    temp_graph[x][y] = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if temp_graph[nx][ny] > rain:
                dfs(nx, ny, rain)


def main(rain):
    count = 0
    for i in range(n):
        for j in range(n):
            if temp_graph[i][j] > rain:
                count += 1
                dfs(i, j, rain)

    return count


if __name__ == "__main__":
    n = int(input().strip())
    max_rain = 0
    graph = []
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        max_rain = max(max_rain, max(line))
        graph.append(line)

    max_count = 0
    for i in range(0, max_rain):
        temp_graph = deepcopy(graph)
        count = main(i)
        max_count = max(max_count, count)

    print(max_count)
