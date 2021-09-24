def main():
    remain = n
    number = 1
    count = 0

    while remain >= 0:
        remain -= number
        number += 1
        count += 1

    print(count - 1)


if __name__ == "__main__":
    n = int(input())

    main()
