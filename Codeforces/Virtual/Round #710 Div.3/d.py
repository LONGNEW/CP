import sys
from heapq import heappop, heappush

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    temp = dict()
    counts = []

    for item in data:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1

    for item in temp.keys():
        heappush(counts, -temp[item])

    while len(counts) > 1:
        a = -heappop(counts) - 1
        b = -heappop(counts) - 1

        if a > 0:
            heappush(counts, -a)
        if b > 0:
            heappush(counts, -b)

    print(0 if len(counts) == 0 else -counts[0])
