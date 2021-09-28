from collections import deque


def main():
    q = deque()
    q.append((a, 1))
    while q:
        now, cnt = q.popleft()
        next_1, next_2 = now * 2, now * 10 + 1

        if next_1 == b:
            print(cnt + 1)
            return
        elif next_1 < b:
            q.append((next_1, cnt + 1))

        if next_2 == b:
            print(cnt + 1)
            return
        elif next_2 < b:
            q.append((next_2, cnt + 1))
    
    print(-1)


if __name__ == "__main__":
    a, b = map(int, input().split())

    main()
