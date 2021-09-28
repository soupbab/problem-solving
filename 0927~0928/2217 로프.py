import sys


def main():
    ropes.sort()
    answer = 0
    for i in range(n):
        answer = max(answer, ropes[i] * (n - i))

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    ropes = [int(input()) for _ in range(n)]

    main()
