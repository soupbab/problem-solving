import sys


def make_dp():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(n):
        for start in range(n - gap):
            if gap == 0:
                dp[start][start + gap] = 1
            elif gap == 1:
                if numbers[start] == numbers[start + gap]:
                    dp[start][start + gap] = 1
            else:
                if numbers[start] == numbers[start + gap] and dp[start + 1][start + gap - 1] == 1:
                    dp[start][start + gap] = 1

    return dp


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = make_dp()
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])
