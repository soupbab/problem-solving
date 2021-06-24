import sys
sys.setrecursionlimit(50000)


def dfs(y, x):
    field[y][x] = 0

    if x > 0 and field[y][x - 1] == 1:
        dfs(y, x - 1)
    if x < m - 1 and field[y][x + 1] == 1:
        dfs(y, x + 1)
    if y > 0 and field[y - 1][x] == 1:
        dfs(y - 1, x)
    if y < n - 1 and field[y + 1][x] == 1:
        dfs(y + 1, x)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        field[y][x] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:
                count += 1
                dfs(j, i)
    
    print(count)