import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())
tomatoes = []
for _ in range(n):
    tomatoes.append(list(map(int, sys.stdin.readline().strip().split())))

ripe_all = True
q = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append((i, j, 0))
        if tomatoes[i][j] == 0 and ripe_all:
            ripe_all = False

if ripe_all:
    print(0)
else:
    day = 0
    while q:
        i, j, day = q.popleft()

        if i > 0 and tomatoes[i - 1][j] == 0:
            tomatoes[i - 1][j] = day + 1
            q.append((i - 1, j, day + 1))
        if i < n - 1 and tomatoes[i + 1][j] == 0:
            tomatoes[i + 1][j] = day + 1
            q.append((i + 1, j, day + 1))
        if j > 0 and tomatoes[i][j - 1] == 0:
            tomatoes[i][j - 1] = day + 1
            q.append((i, j - 1, day + 1))
        if j < m - 1 and tomatoes[i][j + 1] == 0:
            tomatoes[i][j + 1] = day + 1
            q.append((i, j + 1, day + 1))

    for row in tomatoes:
        if 0 in row:
            day = -1

    print(day)