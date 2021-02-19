import sys

n, m = map(int, sys.stdin.readline().split())
edge = [{}for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if b in edge[a]:
        if c < edge[a][b]:
            edge[a][b] = c
    else:
        edge[a][b] = c


def dfs(start, now):
    global temp, cnt;
    next_nodes = edge[now].keys()
    for next_node in next_nodes:
        if visit[next_node] == 0:

            temp += edge[now][next_node]
            visit[next_node] = 1

            dfs(start, next_node)

            visit[next_node] = 0
            temp -= edge[now][next_node]

        if next_node == start:
            cnt = min(cnt, temp + edge[now][next_node])


for i in range(1, n + 1):
    visit = [0] * (n + 1)
    visit[i] = 1
    temp = 0
    cnt = 999999
    dfs(i, i)
    if cnt == 999999:
        print(-1)
    else:
        print(cnt)