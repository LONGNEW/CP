import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
occupied = []
vacant = []

for idx, item in enumerate(data):
    if item == 1:
        occupied.append(idx + 1)
    else:
        vacant.append(idx + 1)

if not occupied:
    print(0)
    exit(0)

dp = [[float('INF')] * (len(vacant) + 1) for i in range(len(occupied) + 1)]

for j in range(len(vacant)):
    dp[1][j + 1] = min(dp[1][j], abs(occupied[0] - vacant[j]))

for i in range(1, len(occupied)):
    for j in range(i, len(vacant)):
        dp[i + 1][j + 1] = min(dp[i][j] + abs(occupied[i] - vacant[j]), dp[i + 1][j])
print(dp[-1][-1])