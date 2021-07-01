import sys


def main():
    dp = [0] * n
    dp[0] = wines[0]
    if n > 1:
        dp[1] = wines[0] + wines[1]
    if n > 2:
        dp[2] = max(wines[0], wines[1]) + wines[2]
    if n > 3:
        dp[3] = wines[0] + max(wines[1], wines[2]) + wines[3]
    if n > 4:    
        for i in range(4, n):
            dp[i] = max(dp[i - 2], dp[i - 3] + wines[i - 1], dp[i - 4] + wines[i - 1]) + wines[i]

    print(max(dp))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    wines = [int(input()) for _ in range(n)]

    main()
