import sys


def Z(scale, row, column, count):
    next_scale = scale - 1
    half = 2 ** next_scale  # 그래프 길이(2^N)의 절반
    unit = half ** 2  # 그래프를 4개로 나눴을 때 한 그래프의 크기

    if row >= half:
        count += 2 * unit
        row -= half
    if column >= half:
        count += unit
        column -= half

    if next_scale > 0:
        return Z(next_scale, row, column, count)
    else:
        return count


def main():
    count = 0
    answer = Z(N, r, c, count)
    
    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, r, c = map(int, input().split())

    main()
