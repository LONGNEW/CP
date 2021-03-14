import sys
from heapq import heappop, heappush

n, m, x, y = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dp = [float('inf')] * n

q = []
heappush(q, (0, y))
dp[y] = 0

while q:
    dis, now_node = heappop(q)

    if dp[now_node] < dis:
        continue

    for next_node, next_cost in graph[now_node]:
        cost = next_cost + dis
        if dp[next_node] > cost:
            dp[next_node] = cost
            heappush(q, (cost, next_node))

for i in range(len(dp)):
    dp[i] *= 2

dp.sort()
if max(dp) > x:
    print(-1)
    exit()

now, ans = 0, 1
for item in dp:
    if now + item > x:
        ans += 1
        now = 0
    now += item
print(ans)
