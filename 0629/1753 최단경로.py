import sys
import heapq


def dijkstra():
    distances = [1e9] * (v + 1)

    q = []
    heapq.heappush(q, (0, k))
    distances[k] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distances[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distances[i[0]] = cost

    for distance in distances[1:]:
        print(distance if distance < 1e9 else "INF")


if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().strip().split())
    k = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, c))

    dijkstra()
