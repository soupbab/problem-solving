import sys


def dfs(x, y, area):
    graph[y][x] = 0
    area[-1] += 1

    if y > 0 and graph[y - 1][x] == 1:
        dfs(x, y - 1, area)
    if y < n - 1 and graph[y + 1][x] == 1:
        dfs(x, y + 1, area)
    if x > 0 and graph[y][x - 1] == 1:
        dfs(x - 1, y, area)
    if x < n - 1 and graph[y][x + 1] == 1:
        dfs(x + 1, y, area)


def main():
    area = []
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 1:
                area.append(0)
                dfs(x, y, area)

    area.sort()
    print(len(area))
    print("\n".join(map(str, area)))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().rstrip())))

    main()
