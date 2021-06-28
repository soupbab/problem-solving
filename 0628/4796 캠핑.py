import sys


def camping(n, l, p, v):
    div, mod = divmod(v, p)
    day = div * l + min(mod, l)

    print(f"Case {n}: {day}")


if __name__ == "__main__":
    n = 1
    while True:
        l, p, v = map(int, sys.stdin.readline().strip().split())
        if l + p + v == 0:
            break
        else:
            camping(n, l, p, v)
            n += 1
