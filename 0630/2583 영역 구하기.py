import sys
sys.setrecursionlimit(15000)


def dfs(x, y, area):
    paper[y][x] = 1
    area[-1] += 1

    if y > 0 and paper[y - 1][x] == 0:
        dfs(x, y - 1, area)
    if y < m - 1 and paper[y + 1][x] == 0:
        dfs(x, y + 1, area)
    if x > 0 and paper[y][x - 1] == 0:
        dfs(x - 1, y, area)
    if x < n - 1 and paper[y][x + 1] == 0:
        dfs(x + 1, y, area)


def main():
    area = []
    for y in range(m):
        for x in range(n):
            if paper[y][x] == 0:
                area.append(0)
                dfs(x, y, area)

    area.sort()
    print(len(area))
    print(" ".join(map(str, area)))


if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, k = map(int, input().split())
    paper = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(m - y2, m - y1):
            for x in range(x1, x2):
                paper[y][x] = -1

    main()
    