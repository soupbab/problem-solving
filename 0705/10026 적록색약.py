import sys
sys.setrecursionlimit(15000)


def is_blue(pixel):
    if pixel == "B":
        return True
    else:
        return False


def dfs(x, y, visit, color=None, blue=None):
    visit[y][x] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(visit) and 0 <= ny < len(visit):
            if visit[ny][nx] == False:
                if image[ny][nx] == color:
                    dfs(nx, ny, visit, color=color)
                if blue is not None and is_blue(image[ny][nx]) is blue:
                    dfs(nx, ny, visit, blue=blue)


def main():
    counts = []
    for i in range(2):
        visit = [[False for _ in range(n)] for _ in range(n)]
        count = 0

        for y in range(n):
            for x in range(n):
                if visit[y][x] == False:
                    if i == 0:
                        dfs(x, y, visit, color=image[y][x])
                    else:
                        dfs(x, y, visit, blue=is_blue(image[y][x]))
                    count += 1
        counts.append(str(count))

    print(" ".join(counts))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    image = [list(input().rstrip()) for _ in range(n)]

    main()
