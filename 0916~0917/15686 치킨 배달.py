from itertools import combinations


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    house = []
    chicken = []
    
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append((i, j))
            if city[i][j] == 2:
                chicken.append((i, j))

    comb = combinations(chicken, m)

    total_dist = float("inf")
    for chicken in comb:
        temp_total = 0
        for h in house:
            dist = float("inf")
            for c in chicken:
                dist = min(dist, distance(h, c))
            temp_total += dist
        total_dist = min(total_dist, temp_total)

    print(total_dist)


if __name__ == "__main__":
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    main()
