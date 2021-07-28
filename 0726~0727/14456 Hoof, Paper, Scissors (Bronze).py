import sys


def case(number):
    count = 0
    for a, b in array:
        if number == 0:
            if a == 1 and b == 2:
                count += 1
            elif a == 2 and b == 3:
                count += 1
            elif a == 3 and b == 1:
                count += 1
        elif number == 1:
            if a == 3 and b == 2:
                count += 1
            elif a == 2 and b == 1:
                count += 1
            elif a == 1 and b == 3:
                count += 1
    
    return count


def main():
    candidate = []
    for i in range(2):
        candidate.append(case(i))

    print(max(candidate))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    array = [tuple(map(int, input().split())) for _ in range(n)]

    main()
