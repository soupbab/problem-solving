import sys


def main(case):
    x1, y1, r1, x2, y2, r2 = case

    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        if distance == r1 + r2:
            print(1)
        elif distance > r1 + r2:
            print(0)
        else:
            gap = abs(r1 - r2)

            if gap == distance:
                print(1)
            elif gap > distance:
                print(0)
            else:
                print(2)


if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        main(list(map(int, input().split())))
