import sys


def binary_search():
    start = 1
    end = max(wires)

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for wire in wires:
            count += wire // mid

        if count >= n:
            max_len = mid
            start = mid + 1
        else:
            end = mid - 1
        
    print(max_len)


if __name__ == "__main__":
    k, n = map(int, sys.stdin.readline().strip().split())
    wires = [int(sys.stdin.readline().strip()) for _ in range(k)]

    binary_search()
