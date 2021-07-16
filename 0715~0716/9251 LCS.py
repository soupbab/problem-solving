import sys


def main():
    dp = [[0 for _ in range(len(word_b) + 1)] for _ in range(len(word_a) + 1)]

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    print(dp[-1][-1])


if __name__ == "__main__":
    input = sys.stdin.readline
    word_a = input().rstrip()
    word_b = input().rstrip()

    main()
