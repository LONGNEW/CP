import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    temp = dict()

    ans, idx = [0] * len(data), 1

    for i in range(n):
        if data[i] not in temp:
            temp[data[i]] = [i]
            continue

        temp[data[i]].append(i)

    time = 0
    temp_key = list(temp.keys())
    for key in temp_key:
        cnt, q = 0, deque(temp[key])

        if len(q) < 2:
            continue

        while q and cnt < k:
            ans[q.popleft()] = idx
            idx += 1
            cnt += 1

            if idx == k + 1:
                idx = 1

        time += 1
        del temp[key]

    if idx != 1:
        temp_key = list(temp.keys())
        time += 1

        for key in temp_key:
            ans[temp[key][-1]] = idx
            idx += 1
            del temp[key]

            if idx == k + 1:
                break

    temp_key = list(temp.keys())
    for i in range(len(temp_key) // k * k):
        ans[temp[temp_key[i]][0]] = idx
        idx += 1

        if idx == k + 1:
            idx = 1

        time += 1

    if time == 0:
        for key in temp_key:
            ans[temp[key][0]] = idx
            idx += 1

            if idx == k + 1:
                break

    print(*ans)