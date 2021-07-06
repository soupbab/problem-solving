import sys


def main():
    table = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(w):
        for j in range(blocks[i]):
            table[h - j - 1][i] = 1

    rain = 0
    for row in table:
        start, end = 0, w - 1
        while start < w and row[start] == 0:
            start += 1
        while end >= 0 and row[end] == 0:
            end -= 1
        try:
            rain += row[start:end].count(0)
        except:
            continue

    print(rain)


if __name__ == "__main__":
    input = sys.stdin.readline
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))

    main()
