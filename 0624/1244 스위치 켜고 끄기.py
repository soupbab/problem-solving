import sys

n = int(sys.stdin.readline().strip())
switches = list(map(int ,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
for _ in range(m):
    gender, number = map(int, sys.stdin.readline().strip().split())

    switches[number - 1] = 1 - switches[number - 1]
    if gender == 1:
        for i in range(2, n // number + 1):
            switches[(number * i) - 1] = 1 - switches[(number * i) - 1]
    else:
        count = 0
        for i in range(1, min(number - 1, n - number) + 1):
            if switches[(number - i) - 1] == switches[(number + i) - 1]:
                switches[(number - i) - 1] = 1 - switches[(number - i) - 1]
                switches[(number + i) - 1] = 1 - switches[(number + i) - 1]
            else:
                break

for i in range(n // 20 + 1):
    print(" ".join(map(str, switches[(i * 20):((i + 1) * 20)])))
