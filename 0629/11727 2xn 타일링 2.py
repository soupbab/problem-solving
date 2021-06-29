import sys


def dp(n):
    array = [0] * (n + 1)

    array[1] = 1

    if n > 1:
        array[2] = 3
    
    if n > 2:
        for i in range(3, n + 1):
            array[i] = array[i - 2] * 2 + array[i - 1]

    print(array[n] % 10007)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    dp(n)
