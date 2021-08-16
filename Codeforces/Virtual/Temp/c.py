import sys,os,io
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())
    l_and_r = [[]]
    for i in range(n):
        l_and_r.append(list(map(int, input().split())))

    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [-1] * (n + 1)
    order = []
    temp = deque([1])
    while temp:
        now_node = temp.popleft()
        order.append(now_node)

        for next_node in graph[now_node]:
            if parent[next_node] != -1 or next_node == parent[now_node]:
                continue

            parent[next_node] = now_node
            temp.append(next_node)

    order.reverse()
    left = [0.] * (n + 1)
    right = [0.] * (n + 1)
    for node in order:
        prev = parent[node]

        if prev == -1:
            continue

        parent_left, parent_right = l_and_r[prev][0], l_and_r[prev][1]
        now_left, now_right = l_and_r[node][0], l_and_r[node][1]
        left[prev] += max(left[node] + abs(parent_left - now_left), right[node] + abs(parent_left - now_right))
        right[prev] += max(left[node] + abs(parent_right - now_left), right[node] + abs(parent_right - now_right))

    print(int(max(left[1], right[1])))