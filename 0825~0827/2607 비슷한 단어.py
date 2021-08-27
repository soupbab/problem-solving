import sys
from collections import defaultdict


def main():
    answer = 0

    target_dict = defaultdict(int)
    for alphabet in words[0]:
        target_dict[alphabet] += 1

    for word in words[1:]:
        if abs(len(words[0]) - len(word)) > 1:
            continue

        word_dict = defaultdict(int)
        for alphabet in word:
            word_dict[alphabet] += 1

        gap = 0
        for alphabet in set(list(target_dict.keys()) + list(word_dict.keys())):
            gap += abs(target_dict[alphabet] - word_dict[alphabet])

        if gap < 3:
            answer += 1

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().rstrip())

    main()
