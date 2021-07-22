import sys


def go_nearest(now):
    min_cnt = abs(n - 100)

    for i in range(n * 2 + 100):
        for j in str(i):
            if int(j) in broken:
                break
        else:
            temp_cnt = abs(n - i) + len(str(i))
            min_cnt = min(min_cnt, temp_cnt)

    return min_cnt


def main():
    print(go_nearest(100))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    broken = set(map(int, input().split()))

    main()
