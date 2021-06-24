import sys

numbers = list(map(int, sys.stdin.readline().strip().split()))

while numbers != sorted(numbers):
    for i in range(4):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            print(" ".join(map(str, numbers)))