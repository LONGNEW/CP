import sys

def solve():
    def find(node):
        if parent[node] == node:
            return parent[node]
        parent[node] = find(parent[node])
        return  parent[node]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a < parent_b:
            parent[b] = parent_a
        else:
            parent[a] = parent_b

    sys.stdin.readline()
    n, m = map(int, sys.stdin.readline().split())
    e = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        e.append((u, v, w))

    mask = 0
    for j in range(29, -1, -1):
        mm = mask | (1 << j)
        parent = [i for i in range(n + 1)]
        c = 0

        for u, v, w in e:
            if w & mm == 0:
                if find(u) != find(v):
                    union(u, v)
                    c += 1

        if c == n - 1:
            mask = mm
    print(((1 << 30) - 1) - mask)


def main():
    for i in range(int(sys.stdin.readline())):
        solve()


if __name__ == '__main__':
    main()
