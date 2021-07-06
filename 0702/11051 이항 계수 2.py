import sys


def main():
    dp = [1, 1, 2]
    if n > 2:
        for i in range(3, n + 1):
            dp.append(dp[-1] * i)

    print((dp[n] // (dp[n - k] * dp[k])) % 10007)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())

    main()
