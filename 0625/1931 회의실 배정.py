import sys


def main():
    conferences.sort(key=lambda x: x[0])
    conferences.sort(key=lambda x: x[1])

    count = 0
    time = 0

    for start, end in conferences:
        if start >= time:
            count += 1
            time = end

    print(count)


if __name__ == "__main__":
    n = int(input().strip())
    conferences = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    main()
