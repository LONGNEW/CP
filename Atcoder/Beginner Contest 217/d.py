import sys
import array
from bisect import bisect_left

l, q = map(int, sys.stdin.readline().split())
data = array.array('i', [0, l])

for i in range(q):
    c, x = map(int, sys.stdin.readline().split())
    idx = bisect_left(data, x)

    if c == 1:
        data.insert(idx, x)
        continue

    left, right = idx - 1, idx
    print(data[right] - data[left])