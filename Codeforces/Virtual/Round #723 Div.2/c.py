#solution from your_name_

import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ans = []
cnt = 0

for item in data:
    cnt += item
    heappush(ans, item)

    if cnt < 0:
        temp = heappop(ans)
        cnt -= temp
print(len(ans))