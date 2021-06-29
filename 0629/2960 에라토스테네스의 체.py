import sys


def main():
    array = [i for i in range(n + 1)]
    count = 0

    i = 2
    while count < k:
        if array[i] != 0:
            for j in range(i, n + 1, i):
                if array[j] != 0:
                    array[j] = 0
                    count += 1

                    if count == k:
                        print(j)
                        return      
        i += 1         


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())

    main()
