import sys
from collections import deque


def main(m, n, h):
    already_ripe = True
    q = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoes[i][j][k] == 1:
                    q.append((i, j, k, 1))
                elif tomatoes[i][j][k] == 0 and already_ripe:
                    already_ripe = False

    if already_ripe == True:
        print(0)
    else:
        dx = [1, -1 ,0 ,0 ,0, 0]
        dy = [0, 0, 1, -1 ,0 ,0]
        dz = [0, 0, 0, 0, 1, -1]

        while q:
            z, y, x, day = q.popleft()

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                    if tomatoes[nz][ny][nx] == 0:
                        tomatoes[nz][ny][nx] = day + 1
                        q.append((nz, ny, nx, day + 1))

        for i in range(h):
            for j in range(n):
                if 0 in tomatoes[i][j]:
                    print(-1)
                    return

        print(day - 1)
                    

if __name__ == "__main__":
    m, n, h = map(int, input().strip().split())
    tomatoes = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]

    main(m, n, h)
    