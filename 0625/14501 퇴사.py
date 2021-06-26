import sys


def consulting(day):
    if day >= len(schedule):
        return 0

    time, profit = schedule[day]
    if day + time > len(schedule):
        return 0
    else:
        return max(profit + consulting(day + time), consulting(day + 1))


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    schedule = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    day = 0
 
    money = consulting(day)

    # print(money)
    a = 3 + 1
    b = 4 + 0
    print(max(a, b))