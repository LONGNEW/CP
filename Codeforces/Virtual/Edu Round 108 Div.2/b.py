import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    ans = [[float('INF')] * (m + 1) for i in range(n + 1)]
    ans[1][1] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < n:
                ans[i + 1][j] = min(ans[i + 1][j], j + ans[i][j])
            if j < m:
                ans[i][j + 1] = min(ans[i][j + 1], i + ans[i][j])

    print("YES" if ans[-1][-1] == k else "NO")