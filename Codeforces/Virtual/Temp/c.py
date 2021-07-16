import sys

n, k, x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

cnt = 0
temp = []

for i in range(len(data) - 1):
    if data[i + 1] - data[i] > 0:
        temp.append((data[i + 1] - data[i] - 1) // x)
        cnt += (data[i + 1] - data[i] - 1) // x

ans = 1
temp.sort()
while cnt > k:
    cnt -= temp.pop()
    ans += 1

print(ans)
