import sys


def main():
    array_a.sort()
    answer = 0
    for a in array_a:
        max_idx, max_val = -1, -1
        for i, b in enumerate(array_b):
            if b == max(max_val, b):
                max_val = b
                max_idx = i
        max_b = array_b.pop(max_idx)
        answer += a * max_b

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))

    main()
