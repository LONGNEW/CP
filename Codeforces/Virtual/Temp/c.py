import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ans, total = [], 0

for item in data:
    heappush(ans, item)
    total += item

    if total < 0:
        total -= heappop(ans)
print(len(ans))