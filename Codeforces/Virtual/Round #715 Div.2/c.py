import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
dp = [[0] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        dp[i][j] = data[j] - data[i] + min(dp[i + 1][j], dp[i][j - 1])

print(dp[0][-1])