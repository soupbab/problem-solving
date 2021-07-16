import sys


def main(n, numbers):
    numbers.sort()
    for i in range(n - 1):
        length = min(len(numbers[i]), len(numbers[i + 1]))
        if numbers[i][:length] == numbers[i + 1][:length]:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [input().rstrip() for _ in range(n)]

        main(n, numbers)
