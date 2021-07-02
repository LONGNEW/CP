import sys

n, k, x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
temp = []
data.sort()

cnt = 0
for i in range(1, len(data)):
    term = (data[i] - data[i - 1] - 1) // x
    if term > 0:
        temp.append(term)
        cnt += term

temp.sort()
idx = len(temp) - 1
while cnt > k:
    cnt -= temp[idx]
    idx -= 1

print(len(temp) - idx)