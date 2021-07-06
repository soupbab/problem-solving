import sys


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


def main():
    array_f.sort()
    array_c.sort()

    min_destroy = 1e9
    count = 0
    for i in range(1, h + 1):
        temp_destroy = 0

        if i <= array_f[-1]:
            temp_destroy += len(array_f) - binary_search(array_f, i)

        reverse_i = h - i + 1
        if reverse_i <= array_c[-1]:
            temp_destroy += len(array_c) - binary_search(array_c, reverse_i)

        if min_destroy == temp_destroy:
            count += 1
        else:
            min_destroy = min(min_destroy, temp_destroy)
            if min_destroy == temp_destroy:
                count = 1

    print(min_destroy, count)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, h = map(int, input().split())
    array_f, array_c = [], []
    for i in range(n):
        if i % 2 == 0:
            array_f.append(int(input()))
        else:
            array_c.append(int(input()))
    
    main()
