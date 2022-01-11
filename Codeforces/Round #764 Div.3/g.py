import sys
from heapq import heappop, heappush

def find(node):
    if parent[node] == node:
        return parent[node]
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parent[b] = parent_a
    else:
        parent[a] = parent_b

t = int(sys.stdin.readline())

for _ in range(t):
    vacant = sys.stdin.readline()
    n, m = map(int, sys.stdin.readline().split())
    edge = []
    parent = [i for i in range(n + 1)]
    ans = 1

    for i in range(m):
        v, u, w = map(int, sys.stdin.readline().split())
        heappush(edge, (w, v, u))

    while edge:
        w, v, u = heappop(edge)

        if find(v) != find(u):
            union(v, u)
            ans |= w
    print(ans)
