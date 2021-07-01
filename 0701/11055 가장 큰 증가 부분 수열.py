import sys


def main():
    dp = [0] * n
    dp[0] = sequence[0]
    for i in range(1, n):
        max_accum = 0
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                max_accum = max(max_accum, dp[j])
        dp[i] = max_accum + sequence[i]

    print(max(dp))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sequence = list(map(int, input().split()))

    main()
    