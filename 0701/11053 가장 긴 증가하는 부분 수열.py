import sys


def main():
    dp = [1] * n
    for i in range(1, n):
        max_len = 0
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                max_len = max(max_len, dp[j])
            dp[i] = max_len + 1

    print(max(dp))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sequence = list(map(int, input().split()))

    main()
    