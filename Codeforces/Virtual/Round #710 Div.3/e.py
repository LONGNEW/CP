import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    ans_min, ans_max = [], []
    for_min, for_max = deque([]), []

    now, equal_num = 1, 0
    while equal_num < n:
        ans_min.append(data[equal_num])
        ans_max.append(data[equal_num])

        while now < data[equal_num]:
            for_min.append(now)
            for_max.append(now)
            now += 1
        now += 1

        idx = equal_num + 1
        while idx < n and data[equal_num] == data[idx]:
            idx += 1

        for i in range(equal_num + 1, idx):
            ans_min.append(for_min.popleft())
            ans_max.append(for_max.pop())

        equal_num = idx

    print(*ans_min)
    print(*ans_max)