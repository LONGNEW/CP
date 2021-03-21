import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

ans = -201
for i in range(b, a - 1, - 1):
    for j in range(d, c - 1, -1):
        ans = max(i - j, ans)

print(ans)