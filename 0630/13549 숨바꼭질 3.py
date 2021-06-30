import sys
import heapq


def main():
    dp = [-1] * 100001
    dp[n] = 0
    heap = [(0, n)]

    while dp[k] == -1:
        count, now = heapq.heappop(heap)

        if now != 0:
            teleport = now * 2    
            while teleport <= 100000 and dp[teleport] == -1:
                dp[teleport] = dp[now]
                heapq.heappush(heap, (count, teleport))
                teleport *= 2
        if now > 0 and dp[now - 1] == -1:
            dp[now - 1] = dp[now] + 1
            heapq.heappush(heap, (count + 1, now - 1))
        if now < 100000 and dp[now + 1] == -1:
            dp[now + 1] = dp[now] + 1
            heapq.heappush(heap, (count + 1, now + 1))
        
    print(dp[k])


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())

    main()
