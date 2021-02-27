import sys
from math import sqrt, ceil

n = int(sys.stdin.readline())
cnt = 0
n = 2 * n
for i in range(1, ceil(sqrt(n))):
    if n % i == 0 and i % 2 != (n // i) % 2:
        cnt += 2
print(cnt)