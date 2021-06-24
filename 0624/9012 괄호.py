import sys


def check_func(data):
    vps = True
    degree = 0
    for d in data:
        if d =="(":
            degree += 1
        else:
            degree -= 1

        if degree < 0:
            vps = False
            break

    if degree != 0:
        vps = False

    print("YES" if vps is True else "NO")


t = int(sys.stdin.readline().strip())

for _ in range(t):
    data = sys.stdin.readline().strip()
    check_func(data)