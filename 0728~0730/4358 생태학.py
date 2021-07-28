import sys
from collections import defaultdict


def main():
    list(map(lambda x: print(f"{x[0]} {x[1] / count * 100:.4f}"), sorted(list(tree.items()))))


if __name__ == "__main__":
    input = sys.stdin.readline
    tree = defaultdict(int)
    count = 0
    while True:
        name = input().rstrip()
        if name:
            tree[name] += 1
            count += 1
        else:
            break

    main()
