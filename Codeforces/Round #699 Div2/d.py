import sys

n = int(input())
a = [int(x) - 1 for x in input().split()]
cnt = [0 for i in range(n)]
l = [-1 for i in range(n)]
r = [-1 for i in range(n)]
for i in range(n):
	cnt[a[i]] += 1
	if l[a[i]] == -1:
		l[a[i]] = i
	r[a[i]] = i
dp = [10**9 for i in range(n + 1)]
ans = n
dp[0] = 0
for i in range(n):
	dp[i + 1] = min(dp[i + 1], dp[i] + 1)
	if l[a[i]] == i:
		dp[r[a[i]] + 1] = min(dp[r[a[i]] + 1], dp[i] + r[a[i]] - i + 1 - cnt[a[i]])
	ans = min(ans, dp[i] + n - i - cnt[a[i]])
	cnt[a[i]] -= 1
print(min(ans, dp[n]))