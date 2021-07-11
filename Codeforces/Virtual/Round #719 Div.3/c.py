import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = [[0] * n for j in range(n)]

    if n == 2:
        print(-1)
        continue

    cur = 1
    for i in range(n):
        for j in range(i % 2, n, 2):
            ans[i][j] = cur
            cur += 1

    for i in range(n):
        for j in range((i + 1) % 2, n, 2):
            ans[i][j] = cur
            cur += 1

    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()