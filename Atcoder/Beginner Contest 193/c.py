import sys
from math import sqrt,ceil

n = int(sys.stdin.readline())
q = set()
for i in range(2, ceil(sqrt(n)) + 1):
    for j in range(2, n):
        if i ** j > n:
            break
        q.add(i ** j)

print(n - len(q))