import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for i in range(t):
    n = int(input())
    data = [(-1, -1)]

    for j in range(n):
        data.append(tuple(map(float, input().split())))

    graph = [[] for j in range(n + 1)]
    for j in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * (n + 1)
    order = []
    q = [1]
    while q:
        node = q.pop()
        order.append(node)

        for next_node in graph[node]:
            if next_node == parent[node]:
                continue
            parent[next_node] = node
            q.append(next_node)

    order.reverse()
    left = [0.] * (n + 1)
    right = [0.] * (n + 1)
    for node in order:
        prev = parent[node]
        if prev == -1:
            continue

        parent_left, parent_right = data[prev][0], data[prev][1]
        node_left, node_right = data[node][0], data[node][1]

        left[prev] += max(left[node] + abs(parent_left - node_left), right[node] + abs(parent_left - node_right))
        right[prev] += max(left[node] + abs(parent_right - node_left), right[node] + abs(parent_right - node_right))

    print(int(max(left[1], right[1])))