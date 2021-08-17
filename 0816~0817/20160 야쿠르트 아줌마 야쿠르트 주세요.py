import sys
import heapq


def dijkstra(start):
    distance = [float("inf")] * (v+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distance


def getTime_y():
    time_arr = [-1] * (v+1)
    time = 0
    now = route[0]
    for r in route:
        distance = dijkstra(now)

        if distance[r] != float("inf"):
            time += distance[r]
            now = r
            time_arr[r] = time

    return time_arr[1:]


def main():
    arrivalTime_y = getTime_y()
    arrivalTime_m = dijkstra(start)[1:]

    for i in range(v):
        if arrivalTime_m[i] <= arrivalTime_y[i]:
            print(i+1)
            return
    print(-1)


if __name__ == "__main__":
    input = sys.stdin.readline
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    route = list(map(int, input().split()))
    start = int(input())

    main()
