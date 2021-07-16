import sys
from collections import deque


def bfs(visit):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visit[0][0] = 0
    q = deque([(0, 0, 0)])
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[ny][nx] == "0" and visit[ny][nx] > cnt:
                    visit[ny][nx] = cnt
                    q.append((nx, ny, cnt))
                if maze[ny][nx] == "1" and visit[ny][nx] > cnt + 1:
                    visit[ny][nx] = cnt + 1
                    q.append((nx, ny, cnt + 1))


def main():
    INF = float("inf")
    visit = [[INF for _ in range(n)] for _ in range(m)]

    bfs(visit)
    print(visit[m - 1][n - 1])


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    maze = [input().rstrip() for _ in range(m)]

    main()
