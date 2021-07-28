import sys


def main():
    numbers.sort(reverse=True)
    a, b = 0, 0
    for i in range(n):
        if i % 2 == 0:
            a += numbers[i]
        else:
            b += numbers[i]

    print(a, b)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    numbers = list(map(int, input().split()))

    main()
