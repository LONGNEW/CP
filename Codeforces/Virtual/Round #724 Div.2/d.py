import sys
from heapq import heappop, heappush

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    flag = 0
    left, right = [], []
    median = data[0]

    for i in range(1, n):
        if median == data[i]:
            continue
        elif median > data[i]:
            if left and -left[0] > data[i]:
                flag = 1
                break

            if left and -left[0] == data[i]:
                heappop(left)

            heappush(right, median)
        else:
            if right and right[0] < data[i]:
                flag = 1
                break

            if right and right[0] == data[i]:
                heappop(right)

            heappush(left, -median)

        median = data[i]

    print("NO" if flag == 1 else "YES")