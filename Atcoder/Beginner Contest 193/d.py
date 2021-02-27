import sys

k = int(sys.stdin.readline())
appear = [0] * (10)

s = sys.stdin.readline().strip()
for item in s:
    if item != '#':
        appear[int(item)] += 1

t = sys.stdin.readline().strip()
for item in t:
    if item != '#':
        appear[int(item)] += 1

can = []
for i in range(1, 10):
    for j in range(appear[i], k):
        can.append(i)

for i in range(0, len(can) - 1):
    for j in range(i, len(can)):
