import sys

n, q = map(int, sys.stdin.readline().split())
data = sys.stdin.readline().rstrip()
dp = [0] * (n + 1)

for i in range(len(data)):
    dp[i + 1] = dp[i] + ord(data[i]) - 96

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(dp[r] - dp[l - 1])