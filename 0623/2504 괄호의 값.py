import sys
import re

p_1 = re.compile("([0-9]+\+){2,15}")
p_2 = re.compile("\([0-9]+\+\)")
p_3 = re.compile("\[[0-9]+\+\]")

data = sys.stdin.readline().strip()
data = data.replace("()", "2+")
data = data.replace("[]", "3+")
while True:
    checkpoint = data[:]
    while p_1.search(data) != None:
        m = p_1.search(data)
        sum_ = sum(map(int, (data[m.start():m.end()-1].split("+"))))
        data = data[:m.start()] + str(sum_) + "+" + data[m.end():]
    while p_2.search(data) != None:
        m = p_2.search(data)
        mul = int(data[m.start()+1:m.end()-2]) * 2
        data = data[:m.start()] + str(mul) + "+" + data[m.end():]
    while p_3.search(data) != None:
        m = p_3.search(data)
        mul = int(data[m.start()+1:m.end()-2]) * 3
        data = data[:m.start()] + str(mul) + "+" + data[m.end():]
    if checkpoint == data:
        break

try:
    print(int(data[:-1]))
except:
    print(0)
    