import sys
from collections import defaultdict


def main():
    ab_sum = defaultdict(int)

    for a in array_a:
        for b in array_b:
            ab_sum[a + b] += 1

    count = 0
    for c in array_c:
        for d in array_d:
            target = -(c + d)
            if target in ab_sum:
                count += ab_sum[target]

    print(count)


if __name__ == "__main__":
    n = int(input())
    array_a, array_b, array_c, array_d = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        array_a.append(a)
        array_b.append(b)
        array_c.append(c)
        array_d.append(d)

    main()
