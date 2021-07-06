import sys
from collections import deque


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    table[0][0] = (0, 1, 1)
    q = deque([(0, 0, 1)])
    while q:
        x, y, chance = q.popleft()
        now_state, now_step, _ = table[y][x]

        if x == m - 1 and y == n - 1:
            return table[y][x][1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                next_state, next_step, next_chance = table[ny][nx]

                if next_state == 0:
                    if next_step > now_step + 1 or next_chance < chance:
                        table[ny][nx] = (next_state, now_step + 1, chance)
                        q.append((nx, ny, chance))
                else:
                    if chance == 1 and next_step > now_step:
                        table[ny][nx] = (next_state, now_step + 1, 0)
                        q.append((nx, ny, 0))

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    INF = 1e9
    table = [list(map(lambda x: (int(x), INF, 0), list(input().rstrip()))) for _ in range(n)]

    print(bfs())
