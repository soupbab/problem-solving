def main():
    target = k
    divisor_array = []
    while True:
        for i in range(2, int(target ** 0.5) + 1):
            if target % i == 0:
                divisor_array.append(i)
                target //= i
                break
        else:
            divisor_array.append(target)
            break

    answer = 0
    while len(divisor_array) > 2 ** answer:
        answer += 1

    print(answer)


if __name__ == "__main__":
    k = int(input())

    main()
