import sys
from heapq import heappop, heappush
from collections import deque

q = int(sys.stdin.readline())
data, data_sort = deque(), []

for _ in range(q):
    temp = list(map(int, sys.stdin.readline().split()))

    if len(temp) == 1:
        if temp[0] == 2:
            if data_sort:
                print(heappop(data_sort))
            else:
                print(data.popleft())
        else:
            while data:
                heappush(data_sort, data.pop())
            data = deque()
    else:
        data.append(temp[1])