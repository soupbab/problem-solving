from collections import deque


def main(n):
    q = [i + 1 for i in range(n)]
    move = 0

    while targets:
        target = targets.popleft()

        if q[0] == target:
            q.pop(0)
        else:
            target_pos = q.index(target)
            move += min(target_pos, len(q) - target_pos)
            q = q[target_pos + 1:] + q[:target_pos]

    print(move)
    

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    targets = deque((map(int, input().strip().split())))

    main(n)
