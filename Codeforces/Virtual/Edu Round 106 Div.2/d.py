import sys

n, k = map(int, sys.stdin.readline().split())
ans = []

for i in range(k):
    now = chr(97 + i)
    ans.append(now)

    for j in range(i + 1, k):
        ans.append(now + chr(97 + j))

ans = "".join(ans)

while len(ans) < n:
    ans += ans

print(ans[:n])