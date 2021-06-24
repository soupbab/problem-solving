import sys

n = int(sys.stdin.readline())
p_list = list(map(int, sys.stdin.readline().strip().split()))

p_list.sort()

time, waiting = 0, 0
for p in p_list:
    time += (p + waiting)
    waiting += p

print(time)
