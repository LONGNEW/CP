import sys
from collections import Counter

n, k = map(int, sys.stdin.readline().split())

for i in range(k):
    count = Counter(str(n))
    temp = sorted(count.elements())
    g1, g2 = '', ''
    for j in range(len(temp)):
        g1_idx, g2_idx = len(temp) - 1 - j, j
        g1 += temp[g1_idx]
        g2 += temp[g2_idx]

    n = int(g1) - int(g2)

print(n)