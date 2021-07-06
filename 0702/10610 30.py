import sys


def main():
    if int(n) % 30 == 0:
        print(n)
    else:
        print(-1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = "".join(sorted(list(input().strip()), reverse=True))

    main()
