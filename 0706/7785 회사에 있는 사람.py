import sys
from collections import defaultdict


def main():
    array = [name for name in log if log[name] == 1]
    array.sort(reverse=True)

    for name in array:
        print(name)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    log = defaultdict(int)
    for _ in range(n):
        name, state = input().split()
        if state == "enter":
            log[name] += 1
        else:
            log[name] -= 1

    main()
