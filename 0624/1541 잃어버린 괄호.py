import sys

data = sys.stdin.readline().strip()

split_minus = data.split("-")
numbers = []
for d in split_minus:
    if "+" in d:
        numbers.append(sum(map(int, d.split("+"))))
    else:
        numbers.append(int(d))

answer = numbers[0]
for number in numbers[1:]:
    answer -= number

print(answer)
