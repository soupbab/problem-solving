import sys
from collections import defaultdict


def main():
    array = [i for i in name.keys() if name[i] == 2]
    array.sort()
    print(len(array))
    print("\n".join(array))


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    name = defaultdict(int)
    for _ in range(n + m):
        name[input().rstrip()] += 1

    main()
