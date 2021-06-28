import sys
import heapq


def abs_heap(num):
    if num == 0:
            if heap:
                target = heapq.heappop(heap)
                if target == int(target):
                    print(-1 * target)
                else:
                    print(int(target))
            else:
                print(0)
    else:
        if num > 0:
            heapq.heappush(heap, num + 0.5)
        else:
            heapq.heappush(heap, -1 * num)


if __name__ == "__main__":
    n = int(input().strip())
    heap = []
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        abs_heap(num)
