import sys
from itertools import combinations
from copy import deepcopy


def dfs(x, y, temp_lab):
    temp_lab[y][x] = 2

    if y > 0 and temp_lab[y - 1][x] == 0:
        dfs(x, y - 1, temp_lab)
    if y < n - 1 and temp_lab[y + 1][x] == 0:
        dfs(x, y + 1, temp_lab)
    if x > 0 and temp_lab[y][x - 1] == 0:
        dfs(x - 1, y, temp_lab)
    if x < m - 1 and temp_lab[y][x + 1] == 0:
        dfs(x + 1, y, temp_lab)


def main():
    candidates = []
    for y in range(n):
        for x in range(m):
            if laboratory[y][x] == 0:
                candidates.append((x, y))

    nCr = combinations(candidates, 3)

    answer = 0
    for positions in nCr:
        temp_lab = deepcopy(laboratory)
        for x, y in positions:
            temp_lab[y][x] = 1

        for y in range(n):
            for x in range(m):
                if temp_lab[y][x] == 2:
                    dfs(x, y, temp_lab)

        safe_area = 0
        for y in range(n):
            for x in range(m):
                if temp_lab[y][x] == 0:
                    safe_area += 1

        answer = max(answer, safe_area)

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    laboratory = [list(map(int, input().split())) for _ in range(n)]

    main()
