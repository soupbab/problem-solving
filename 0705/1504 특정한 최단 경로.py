import sys
import heapq


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distance


def main():
    start_ = dijkstra(1)
    v1_ = dijkstra(v1)
    v2_ = dijkstra(v2)

    root = min(start_[v1] + v1_[v2] + v2_[n], start_[v2] + v2_[v1] + v1_[n])

    print(root if root < INF else -1) 


if __name__ == "__main__":
    input = sys.stdin.readline
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())

    INF = 1e9
    main()
