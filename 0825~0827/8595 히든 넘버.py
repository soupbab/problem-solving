import re
from functools import reduce


def main():
    hidden_numbers = re.findall("[0-9]+", string)
    answer = reduce(lambda a, b: a + int(b) if len(b) <= 6 else a, hidden_numbers, 0)
    print(answer)


if __name__ == "__main__":
    n = int(input())
    string = input().rstrip()

    main()
