import sys
from math import floor

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    idx, total = [0] * (n + 1), 0

    for item in data:
        if item < n + 1:
            idx[item] += 1
            total += 1

    if idx[1] > 1:
        print("NO")
        continue

    while idx[1] <= 1 and idx[1:].count(0):
        for i in range(len(data)):
            item = data[i]

            if item == 1 or (item < n + 1 and idx[item] == 1):
                continue

            if item < n + 1 and idx[item] > 1:
                idx[item] -= 1
                data[i] = floor(item / 2)
                idx[data[i]] += 1
                continue

            data[i] = floor(item / 2)
            if data[i] < n + 1:
                idx[data[i]] += 1

    if idx[1] > 1:
        print("NO")
    else:
        print("YES")