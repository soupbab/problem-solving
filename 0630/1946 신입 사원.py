import sys


def hire(n, ranks):
    ranks.sort(reverse=True)

    count = 0
    cut_off = n + 1
    while ranks:
        rank_1, rank_2 = ranks.pop()
        if rank_2 < cut_off:
            count += 1
            cut_off = rank_2

    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        ranks = [tuple(map(int, input().split())) for _ in range(n)]   

        hire(n, ranks)
