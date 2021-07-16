import sys


def main():
    weights.sort()
    accum = 0
    for weight in weights:
        if weight <= accum + 1:
            accum += weight
        else:
            break
        
    print(accum + 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    weights = list(map(int, input().split()))

    main()
