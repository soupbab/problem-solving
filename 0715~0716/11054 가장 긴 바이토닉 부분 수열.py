import sys


def main():
    inc_dp = [1] * n
    for i in range(1, n):
        max_len = 1
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                max_len = max(max_len, inc_dp[j] + 1)
        inc_dp[i] = max_len

    max_len = 1
    for i in range(1, n):
        max_len = max(max_len, inc_dp[i])
        inc_dp[i] = max_len

    sequence.reverse()

    dec_dp = [1] * n
    for i in range(1, n):
        max_len = 1
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                max_len = max(max_len, dec_dp[j] + 1)
        dec_dp[i] = max_len

    max_len = 1
    for i in range(1, n):
        max_len = max(max_len, dec_dp[i])
        dec_dp[i] = max_len
    dec_dp.reverse()

    len_array = [inc_dp[i] + dec_dp[i] for i in range(n)]
    print(max(len_array) - 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sequence = list(map(int, input().split()))

    main()
