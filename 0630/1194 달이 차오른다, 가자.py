import sys
from collections import deque


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    maze[y][x] = ("0", 0b0)
    q = deque([(x, y, 0, 0b0)])
    while q:
        x, y, step, keys = q.popleft()

        for i in range(4):
            temp_keys = keys
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:  # 다음 위치가 지도 범위 내에 있다면 진행.
                next_state, next_keys = maze[ny][nx]  # 다음 위치의 상태, 해당 위치를 마지막으로 통과했을 때의 열쇠 상태.
                # 다음 위치가 지나갈 수 있는 길인지 판별.
                if next_state == "1":  # 도착지인 경우: 걸음 수를 반환.
                    return step + 1
                elif next_state == "#":  # 벽인 경우: continue.
                    continue
                else:
                    if next_state in "abcdef":  # 열쇠인 경우: 소지 중인 열쇠를 갱신.
                        shift = ord(next_state) - 97
                        temp_keys = temp_keys | (0b1 << shift)
                    elif next_state in "ABCDEF":  # 문인 경우에는,
                        shift = ord(next_state) - 65
                        shifted = 0b1 << shift

                        if temp_keys & shifted != shifted:  # 맞는 열쇠가 없으면 continue.
                            continue                     
                # 다음 위치가 지나갈 수 있는 길이라고 판단된 경우 진행.
                if (
                    next_keys is not None  # 이미 지나갔던 길인데,
                    and (temp_keys | next_keys) == next_keys  # 열쇠를 더 들고오지도 않은 경우 continue.
                ):  
                    continue
                    
                maze[ny][nx] = (next_state, temp_keys)  # 다음 위치의 열쇠 상태를 현재 소지 중인 열쇠로 갱신.
                q.append((nx, ny, step + 1, temp_keys))  # 다음 위치와 걸음 수, 열쇠 상태를 큐에 추가.

    return -1


def main():
    for y in range(n):
        for x in range(m):
            if maze[y][x][0] == "0":
                answer = bfs(x, y)
                return print(answer)
                

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    maze = [list(map(lambda x: (x, None), input().rstrip())) for _ in range(n)]

    main()
