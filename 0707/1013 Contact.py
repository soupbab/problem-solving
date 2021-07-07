import sys
import re


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    p = re.compile("(100+1+|01)+")
    for _ in range(n):
        data = input().rstrip()
        if p.fullmatch(data):
            print("YES")
        else:
            print("NO")
    