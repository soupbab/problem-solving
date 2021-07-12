import sys
sys.setrecursionlimit(15000)


def dfs(x, y, dp):
    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if forest[ny][nx] > forest[y][x]:
                dp[y][x] = max(dp[y][x], dfs(nx, ny, dp) + 1)

    return dp[y][x]


def main():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    answer = 1

    for y in range(n):
        for x in range(n):
            answer = max(answer, dfs(x, y, dp))

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    forest = [list(map(int, input().split())) for _ in range(n)]

    main()
