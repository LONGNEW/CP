import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = [0] * 401

ans = 0
temp[data[0] + 200] += 1
for i in range(1, len(data)):
    for idx, item in enumerate(temp):
        if item != 0:
            ans += item * (idx - 200 - data[i]) ** 2
    temp[data[i] + 200] += 1

print(ans)