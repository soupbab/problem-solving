from itertools import permutations


def calculate():
    operators_list = []
    for i in range(4):
        operators_list.extend([i] * operator_counts[i])
    nPr = permutations(operators_list)

    maximum = -1e9
    minimum = 1e9

    for operators in nPr:
        number = numbers[0]
        for i in range(n - 1):
            if operators[i] == 0:
                number += numbers[i + 1]
            elif operators[i] == 1:
                number -= numbers[i + 1]
            elif operators[i] == 2:
                number *= numbers[i + 1]
            else:
                if number >= 0:
                    number //= numbers[i + 1]
                else:
                    number = -1 * (-1 * number // numbers[i + 1])

        maximum = max(maximum, number)
        minimum = min(minimum, number)

    print(maximum)
    print(minimum)


if __name__ == "__main__":
    n = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    operator_counts = list(map(int, input().strip().split()))

    calculate()

# 참고하면 좋을 코드 https://www.acmicpc.net/source/10510964