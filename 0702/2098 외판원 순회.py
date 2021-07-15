import sys


def find_path(now, visited, dp):
    INF = float("inf")

    if visited == (1 << n) - 1:
        return graph[now][0] or INF

    if dp[now][visited] is not None:
        return dp[now][visited]

    dist = INF
    for city in range(n):
        if visited & (1 << city) == 0 and graph[now][city] != 0:
            dist = min(dist, graph[now][city] + find_path(city, visited | (1 << city), dp))
    dp[now][visited] = dist
    return dist


def main():
    dp = [[None] * (1 << n) for _ in range(n)]

    print(find_path(0, 1, dp))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    main()
