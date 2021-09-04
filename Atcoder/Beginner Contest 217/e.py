import sys
from collections import deque

q = int(sys.stdin.readline())
data = deque()
data_small =
for _ in range(q):
    temp = list(map(int, sys.stdin.readline().split()))

    if len(temp) == 1:
        if temp[0] == 2:
            now = data.popleft()
            print(now)
        else:
            data = deque(sorted(list(data)))
    else:
        data.append(temp[1])
