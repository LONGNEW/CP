import sys

n = int(sys.stdin.readline())
data = []
ans = float('inf')
for i in range(n):
    a, p, x = map(int, sys.stdin.readline().split())
    left = x - a
    if left > 0:
        ans = min(ans, p)

print(-1 if ans == float('inf') else ans)
