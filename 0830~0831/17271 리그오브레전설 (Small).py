from functools import reduce


def nCr(n, r):
    r = min(r, n - r)
    numerator = reduce(lambda a, b: a * b, range(n, n - r, -1), 1)
    denominator = reduce(lambda a, b: a * b, range(r, 0, -1), 1)

    return numerator // denominator


def main():
    answer = 0
    cnt_a = n
    cnt_b = 0

    while n >= m * cnt_b:
        answer += nCr(cnt_a + cnt_b, cnt_b)
        cnt_a -= m
        cnt_b += 1

    print(answer % 1000000007)


if __name__ == "__main__":
    n, m = map(int, input().split())

    main()
