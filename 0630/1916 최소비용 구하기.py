import sys
import heapq


def dijkstra(start, goal):
    INF = 1e9
    distances = [INF] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        dist, now = heapq.heappop(heap)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distances[goal]


def main():
    answer = dijkstra(start, goal)

    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, goal = map(int, input().split())

    main()
