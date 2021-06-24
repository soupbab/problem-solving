import sys

n = int(sys.stdin.readline())

bag_3 = 0
for _ in range(5):
    if n % 5 == 0:
        bag_5 = n // 5
        print(bag_3 + bag_5)
        break
    else:
        if n >= 3:
            bag_3 += 1
            n -= 3
        else:
            print(-1)
            break
