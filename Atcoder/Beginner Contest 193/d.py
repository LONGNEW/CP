import sys
from itertools import combinations

k = int(sys.stdin.readline())
appear = [0] * (10)
Taka = [0] * (10)
Aoki = [0] * (10)
Taka_sum = [0] * (10)
Aoki_sum = [0] * (10)

s = sys.stdin.readline().strip()
for item in s:
    if item != '#':
        appear[int(item)] += 1
        Taka[int(item)] += 1

t = sys.stdin.readline().strip()
for item in t:
    if item != '#':
        appear[int(item)] += 1
        Aoki[int(item)] += 1

can = []
for i in range(1, 10):
    for j in range(appear[i], k):
        can.append(i)

for i in range(1, 10):
    if Taka[i] < k:
        Taka[i] += 1
    else:
        continue

    temp = 0
    for j in range(1, 10):
        num = Taka[j]
        temp += j * (10 ** num)
    Taka_sum[i] = temp
    Taka[i] -= 1

for i in range(1, 10):
    if Aoki[i] < k:
        Aoki[i] += 1
    else:
        continue

    temp = 0
    for j in range(1, 10):
        num = Aoki[j]
        temp += j * (10 ** num)
    Aoki_sum[i] = temp
    Aoki[i] -= 1
