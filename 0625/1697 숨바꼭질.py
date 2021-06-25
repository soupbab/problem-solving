from collections import deque


def main(n, k):
    position = [-1] * 100001
    position[n] = 0
    q = deque([n])

    while position[k] == -1:
        now = q.popleft()

        if now > 0 and position[now - 1] == -1:
            position[now - 1] = position[now] + 1
            q.append(now - 1)
        if now < 100000 and position[now + 1] == -1:
            position[now + 1] = position[now] + 1
            q.append(now + 1)
        if now <= 50000 and position[now * 2] == -1:
            position[now * 2] = position[now] + 1
            q.append(now * 2)

    print(position[k])


if __name__ == "__main__":
    n, k = map(int, input().strip().split())

    main(n, k)
