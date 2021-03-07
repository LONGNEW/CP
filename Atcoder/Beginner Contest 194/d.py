import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(1, n):
    ans += n / n - i
print(ans)