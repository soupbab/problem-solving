import sys


def main():
    dp = [[0 for _ in range(m)] for _ in range(n)]
    max_size = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    
                    if max_size == 0:
                        max_size = 1
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_size = max(max_size, dp[i][j])

    print(max_size ** 2)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    table = [list(map(int, list(input().rstrip()))) for _ in range(n)]

    main()
