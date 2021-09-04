import sys
from bisect import bisect_left

l, q = map(int, sys.stdin.readline().split())
data = [0, l]

for i in range(q):
    c, x = map(int, sys.stdin.readline().split())

    if c == 1:
        data.append(x)
        continue

    data.sort()
    idx = bisect_left(data, x)
    left, right = idx - 1, idx
    print(data[right] - data[left])