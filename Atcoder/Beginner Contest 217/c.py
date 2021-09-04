import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n

for i in range(n):
    ans[data[i] - 1] = i + 1

print(*ans)
