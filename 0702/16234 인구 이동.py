import sys
from collections import defaultdict


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])

    return parent[a]


def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    for i in range(len(parent)):
        if parent[i] == max(parent_a, parent_b):
            parent[i] = min(parent_a, parent_b)


def move(parent):
    unions = defaultdict(list)
    for i in range(len(parent)):
        unions[parent[i]].append(divmod(i, n))
    
    for pos_list in unions.values():

        mean = sum(map(lambda x: world[x[0]][x[1]], pos_list)) // len(pos_list)
        for pos in pos_list:
            world[pos[0]][pos[1]] = mean


def main():
    dx = [0, 1]
    dy = [1, 0]

    count = 0
    while True:
        can_move = False
        parent = [i for i in range(n ** 2)]
        
        for y in range(n):
            for x in range(n):
                for i in range(2):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if l <= abs(world[y][x] - world[ny][nx]) <= r:
                            union_parent(parent, n * y + x, n * ny + nx)

                            if not can_move:
                                can_move = True
        
        if can_move:
            move(parent)
            count += 1
        else:
            break

    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, l, r = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(n)]

    main()
