import sys


def main():
    target = k
    coins.sort(reverse=True)
    answer = 0
    
    for coin in coins:
        div, mod = divmod(target, coin)

        if div > 0:
            answer += div
            target = mod

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k  = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    main()
